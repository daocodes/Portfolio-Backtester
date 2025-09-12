<h1 align="center">📊 StockVision</h1>
<p align="center">
  A full-stack portfolio backtester built with <b>FastAPI</b>, <b>TailwindCSS</b>, and <b>Chart.js</b>.  
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python">
  <img src="https://img.shields.io/badge/FastAPI-0.116.1-teal?logo=fastapi">
  <img src="https://img.shields.io/badge/TailwindCSS-4.0-blue?logo=tailwindcss">
  <img src="https://img.shields.io/badge/Chart.js-5.0-purple?logo=chartdotjs">
</p>

---

## ✨ Demo

🎥 **App Walkthrough**  
_Add a GIF here showing how the app works end-to-end_  

<img src="assets/demo.gif" width="800"/>

---

## 🚀 Features

- 🔍 **Search bar** – Add stocks, ETFs, or crypto to your portfolio  
  <img src="assets/search.png" width="600"/>

- 📈 **Dynamic charts** – Interactive graphs powered by Chart.js  
  <img src="assets/chart.png" width="600"/>

- 🧮 **Strategy templates** – Prebuilt portfolios like 60/40, Permanent Portfolio, FAANG, Dividend Growth  
  <img src="assets/templates.png" width="600"/>

- 📊 **Stats panel** – Displays cumulative return, CAGR, Sharpe ratio, volatility, and drawdown  
  <img src="assets/stats.png" width="600"/>

- 🎨 **Theme modes** – Switch between Dark 🌑, Sunset 🌅, and Pastel 🌸  
  <img src="assets/themes.png" width="600"/>

---


Finance-Project/
│
├── main1.py              # FastAPI backend
├── algo.py               # extra backend logic
├── requirements.txt      # Python dependencies
├── package.json          # npm config (Tailwind)
├── start.sh              # script to run app
├── tailwind.config.js    # Tailwind config
│
├── src/                  # frontend
│   ├── index.html        # landing page
│   ├── graph.html        # main portfolio page
│   ├── api.js            # JS for API calls
│   ├── input.css         # Tailwind source
│   ├── output.css        # built CSS
│   └── wall-street-background.jpg
│
└── assets/               # screenshots & GIFs for README
    ├── demo.gif
    ├── chart.png
    ├── sidebar.png
    ├── stats.png
    └── themes.png

Built by Dao Bui

<p> <a href="https://www.linkedin.com/in/dao-bui-bb53692b4/"> <img src="https://img.shields.io/badge/LinkedIn-Dao%20Bui-blue?logo=linkedin"> </a> </p>
## ⚙️ Installation

Clone the repo:

```bash
git clone https://github.com/YOUR_USERNAME/StockVision.git
cd StockVision

python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt
uvicorn main1:app --reload

npm install
npx tailwindcss -i ./src/input.css -o ./src/output.css --watch



