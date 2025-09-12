# 📊 Backtester 1.0

Backtester is a **finance and portfolio tracking web app** built with **FastAPI (Python)** and **Chart.js + TailwindCSS (frontend)**.  
It helps you visualize assets, run strategies, and switch between custom color themes.

---

## ✨ Preview

![Demo](assets/demo.gif)  
*A quick walkthrough of Backtester 1.0 in action.*

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

## ⚙️ Installation

Clone the repo:
```bash
git clone https://github.com/YOUR_USERNAME/StockVision.git
cd StockVision

python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt

npm install
npx tailwindcss -i ./src/input.css -o ./src/output.css --watch

uvicorn main1:app --reload

```
--- 
## 💭 Reflection

I created this project as a way to teach myself how to build a full-stack application from the ground up. At the same time, I wanted to deepen my understanding of financial concepts, but through the perspective of a software engineer — building tools rather than just reading about them.

Through this project, I learned a lot of CSS and TailwindCSS, how to structure and connect a FastAPI backend with a modern frontend, and how to effectively leverage AI tools to refine, debug, and enhance my application.

This project was as much about learning engineering best practices as it was about exploring finance through software.

