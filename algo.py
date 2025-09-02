# algo.py
import pandas as pd
import yfinance as yf


def portfolio_history(weighting: dict, start_date="2016-01-01"):
    members = list(weighting.keys())

    try:
        # Start with first ticker
        basedata = (
            yf.Ticker(members[0]).history(period="max").reset_index()[["Date", "Open"]]
        )
        basedata = basedata.rename(columns={"Open": members[0]})
        basedata["Date"] = pd.to_datetime(basedata["Date"])

        # Merge rest
        for x in members[1:]:
            newdata = yf.Ticker(x).history(period="max").reset_index()[["Date", "Open"]]
            newdata = newdata.rename(columns={"Open": x})
            newdata["Date"] = pd.to_datetime(newdata["Date"])
            basedata = pd.merge(basedata, newdata, on="Date", how="outer")

        # Clean + normalize
        basedata = basedata.sort_values("Date").interpolate().dropna()
        basedata = basedata[basedata["Date"] > start_date].copy()

        for x in members:
            basedata[x] = basedata[x] / basedata[x].iloc[0]

        # Portfolio calc
        total_weight = sum(weighting.values())
        basedata["My Portfolio"] = 0
        for x in members:
            basedata["My Portfolio"] += (weighting[x] / total_weight) * basedata[x]

        return basedata

    except Exception as e:
        # Return empty DataFrame if anything fails
        return pd.DataFrame(
            {"Date": [], "My Portfolio": [], **{k: [] for k in members}}
        )
