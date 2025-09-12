# 📊 StockVision

StockVision is a **finance and portfolio tracking web app** built with **FastAPI (Python)** and **Chart.js + TailwindCSS (frontend)**.  
It helps you visualize assets, run strategies, and switch between custom color themes.

---

## 🚀 Features
- 🔍 **Search bar** – quickly add stocks, ETFs, or crypto to your portfolio  
- 📈 **Chart visualization** – powered by Chart.js  
- ⚡ **Moving Average Mode** – overlay SMA curves with custom period  
- 🧮 **Strategy Templates** – load prebuilt allocations like:
  - 60/40 Portfolio  
  - Permanent Portfolio  
  - Equal Weight (FAANG)  
  - Dividend Growth  
  - Barbell Strategy  
- 📊 **Stats Panel** – automatic calculation of:
  - Cumulative Return  
  - CAGR (Annualized Return)  
  - Volatility  
  - Sharpe Ratio  
  - Max Drawdown  

---

## 🛠 Tech Stack
**Backend**
- FastAPI  
- yfinance (stock/crypto data)  
- pandas (data processing)  

**Frontend**
- HTML / TailwindCSS  
- Chart.js (graphing library)  
- Vanilla JS  

---

## Additional Information

Created By: Dao Bui

Reflection: I created this to learn how to create a full stack application. I also wanted to learn financial concepts through the lens of a software engineer. Along the way, I learned a ton about CSS and TailwindCSS, how to structure and connect a FastAPI backend with a modern frontend, and how to use AI tools effectively to refine, debug, and enhance my application. This project was as much about learning engineering best practices as it was about exploring finance through software. I'm excited to continue building projects that I am passionate about and enhance my technical ability.

## ⚙️ Installation

Clone the repo:
```bash
git clone https://github.com/YOUR_USERNAME/StockVision.git
cd StockVision

# create a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

# install dependencies
pip install -r requirements.txt
npm install

# build Tailwind
npx tailwindcss -i ./src/input.css -o ./src/output.css --watch

#Start FastAPI server:
uvicorn main1:app --reload

Then open your browser:
http://127.0.0.1:8000

