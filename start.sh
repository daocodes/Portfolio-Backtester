#!/bin/bash

echo "🚀 Starting StockVision Finance Project..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip first."
    exit 1
fi

echo "📦 Installing Python dependencies..."
pip3 install -r requirements.txt

echo "🔨 Building Tailwind CSS..."
npm run build:once

echo "🌐 Starting FastAPI backend..."
echo "   Backend will be available at: http://localhost:8000"
echo "   API documentation at: http://localhost:8000/docs"
echo ""
echo "📱 Frontend is available at: src/index.html"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start FastAPI server
python3 main_simple.py 