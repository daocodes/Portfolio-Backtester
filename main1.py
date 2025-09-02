import numpy as np
import pandas as pd
import requests
import yfinance as yf
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

# Serve frontend
app.mount("/static", StaticFiles(directory="src"), name="static")


@app.get("/")
def serve_index():
    return FileResponse("src/graph.html")


# ------------------------------------
# API: Quote
# ------------------------------------
@app.get("/api/quote/{symbol}")
async def get_quote(symbol: str, period: str = "1mo"):
    try:
        hist = yf.download(symbol, period=period, interval="1d", progress=False)
        if hist.empty:
            raise HTTPException(status_code=404, detail="No data found")

        if isinstance(hist.columns, pd.MultiIndex):
            if ("Close", symbol) in hist.columns:
                prices = hist[("Close", symbol)]
            elif ("Adj Close", symbol) in hist.columns:
                prices = hist[("Adj Close", symbol)]
            else:
                raise HTTPException(
                    status_code=500, detail=f"No price column for {symbol}"
                )
        else:
            prices = hist.get("Close") or hist.get("Adj Close")
            if prices is None:
                raise HTTPException(status_code=500, detail="No price column")

        norm_prices = prices / prices.iloc[0]

        return {
            "symbol": symbol,
            "period": period,
            "dates": hist.index.strftime("%Y-%m-%d").tolist(),
            "prices": norm_prices.round(4).tolist(),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ------------------------------------
# API: Portfolio
# ------------------------------------
class PortfolioRequest(BaseModel):
    weights: dict[str, float]
    period: str = "1y"


@app.post("/api/portfolio-history")
def portfolio_history_endpoint(request: PortfolioRequest):
    try:
        weights = request.weights
        members = list(weights.keys())
        if not members:
            raise HTTPException(status_code=400, detail="No assets provided")

        basedata = (
            yf.Ticker(members[0])
            .history(period=request.period)
            .reset_index()[["Date", "Open"]]
        )
        basedata = basedata.rename(columns={"Open": members[0]})
        basedata["Date"] = pd.to_datetime(basedata["Date"])

        for x in members[1:]:
            newdata = (
                yf.Ticker(x)
                .history(period=request.period)
                .reset_index()[["Date", "Open"]]
            )
            newdata = newdata.rename(columns={"Open": x})
            newdata["Date"] = pd.to_datetime(newdata["Date"])
            basedata = pd.merge(basedata, newdata, on="Date", how="outer")

        basedata = basedata.sort_values("Date").interpolate().dropna()
        for x in members:
            basedata[x] = basedata[x] / basedata[x].iloc[0]

        total_weight = sum(weights.values())
        basedata["My Portfolio"] = 0
        for x in members:
            basedata["My Portfolio"] += (weights[x] / total_weight) * basedata[x]

        # --- Stats ---
        prices = basedata["My Portfolio"]
        cumulative_return = prices.iloc[-1] - 1.0
        daily_returns = prices.pct_change().dropna()
        volatility = daily_returns.std() * np.sqrt(252)
        sharpe = (
            daily_returns.mean() / daily_returns.std() * np.sqrt(252)
            if daily_returns.std() > 0
            else 0
        )
        max_drawdown = ((prices / prices.cummax()) - 1).min()
        num_days = (basedata["Date"].iloc[-1] - basedata["Date"].iloc[0]).days
        years = num_days / 365.25
        cagr = (prices.iloc[-1]) ** (1 / years) - 1 if years > 0 else 0

        return {
            "dates": basedata["Date"].dt.strftime("%Y-%m-%d").tolist(),
            "portfolio": basedata["My Portfolio"].round(4).tolist(),
            "stats": {
                "cumulative_return": round(cumulative_return * 100, 2),
                "cagr": round(cagr * 100, 2),
                "volatility": round(volatility * 100, 2),
                "sharpe": round(sharpe, 2),
                "max_drawdown": round(max_drawdown * 100, 2),
            },
            **{x: basedata[x].round(4).tolist() for x in members},
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ------------------------------------
# API: Search + Trending
# ------------------------------------
HEADERS = {"User-Agent": "Mozilla/5.0"}


@app.get("/api/search/{query}")
def search_symbols(query: str):
    try:
        url = f"https://query2.finance.yahoo.com/v1/finance/search?q={query}"
        r = requests.get(url, headers=HEADERS, timeout=5)
        data = r.json()
        results = data.get("quotes", [])[:5]
        return [
            {
                "symbol": x.get("symbol"),
                "name": x.get("shortname") or x.get("longname") or x.get("symbol"),
                "exchange": x.get("exchange", ""),
                "type": x.get("quoteType", ""),
            }
            for x in results
            if x.get("symbol")
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search failed: {e}")


@app.get("/api/trending")
def trending_assets():
    try:
        url = "https://query1.finance.yahoo.com/v1/finance/trending/US"
        r = requests.get(url, headers=HEADERS, timeout=5)
        data = r.json()
        results = data.get("finance", {}).get("result", [{}])[0].get("quotes", [])
        top = [{"symbol": x.get("symbol")} for x in results[:5] if x.get("symbol")]
        return top
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Trending fetch failed: {e}")
