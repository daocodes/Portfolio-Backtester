#!/bin/bash
# Install npm packages (for Tailwind)
npm install

# Build Tailwind CSS into output.css
npx tailwindcss -i ./src/input.css -o ./src/output.css

# Start FastAPI backend
uvicorn main1:app --host 0.0.0.0 --port $PORT
