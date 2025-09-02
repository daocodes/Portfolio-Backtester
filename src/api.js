// API configuration
const API_BASE_URL = 'http://localhost:8000/api';

// API utility functions
class StockVisionAPI {
    constructor() {
        this.baseURL = API_BASE_URL;
    }

    // Generic fetch wrapper with error handling
    async fetchAPI(endpoint, options = {}) {
        try {
            const response = await fetch(`${this.baseURL}${endpoint}`, {
                headers: {
                    'Content-Type': 'application/json',
                    ...options.headers
                },
                ...options
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            return await response.json();
        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    }

    // Get all stocks
    async getStocks() {
        return this.fetchAPI('/stocks');
    }

    // Get specific stock by symbol
    async getStock(symbol) {
        return this.fetchAPI(`/stocks/${symbol}`);
    }

    // Get user portfolio
    async getPortfolio(userId) {
        return this.fetchAPI(`/portfolio/${userId}`);
    }

    // Add stock to portfolio
    async addStockToPortfolio(userId, stockData) {
        return this.fetchAPI(`/portfolio/${userId}/add`, {
            method: 'POST',
            body: JSON.stringify(stockData)
        });
    }

    // Get market summary
    async getMarketSummary() {
        return this.fetchAPI('/market-summary');
    }

    // Search stocks
    async searchStocks(query) {
        return this.fetchAPI(`/search/${query}`);
    }

    // Health check
    async healthCheck() {
        return this.fetchAPI('/health');
    }
}

// Create global API instance
const api = new StockVisionAPI();

// Example usage functions
async function displayStocks() {
    try {
        const data = await api.getStocks();
        console.log('Stocks:', data.stocks);
        
        // You can update your HTML here with the stock data
        updateStockDisplay(data.stocks);
    } catch (error) {
        console.error('Failed to fetch stocks:', error);
    }
}

async function displayMarketSummary() {
    try {
        const data = await api.getMarketSummary();
        console.log('Market Summary:', data);
        
        // Update market summary display
        updateMarketSummaryDisplay(data);
    } catch (error) {
        console.error('Failed to fetch market summary:', error);
    }
}

// UI update functions
function updateStockDisplay(stocks) {
    // Example: Update a stock list in your HTML
    const stockContainer = document.getElementById('stock-list');
    if (stockContainer) {
        stockContainer.innerHTML = stocks.map(stock => `
            <div class="stock-item border border-white p-4 m-2">
                <h3 class="text-xl font-bold">${stock.symbol}</h3>
                <p class="text-lg">$${stock.price.toFixed(2)}</p>
                <p class="${stock.change >= 0 ? 'text-green-400' : 'text-red-400'}">
                    ${stock.change >= 0 ? '+' : ''}${stock.change.toFixed(2)} (${stock.change_percent.toFixed(2)}%)
                </p>
                <p class="text-sm">Volume: ${stock.volume.toLocaleString()}</p>
            </div>
        `).join('');
    }
}

function updateMarketSummaryDisplay(summary) {
    // Example: Update market summary display
    const summaryContainer = document.getElementById('market-summary');
    if (summaryContainer) {
        summaryContainer.innerHTML = `
            <div class="market-summary border border-white p-6 m-4">
                <h2 class="text-2xl font-bold mb-4">Market Summary</h2>
                <p>Total Market Cap: $${(summary.total_market_cap / 1e12).toFixed(2)}T</p>
                <p>Total Volume: ${summary.total_volume.toLocaleString()}</p>
                <p>Stocks Count: ${summary.stocks_count}</p>
                <p class="text-sm text-gray-400">Last Updated: ${new Date(summary.timestamp).toLocaleString()}</p>
            </div>
        `;
    }
}

// Initialize API connection when page loads
document.addEventListener('DOMContentLoaded', async () => {
    try {
        // Test API connection
        const health = await api.healthCheck();
        console.log('API Status:', health.status);
        
        // Load initial data
        await displayStocks();
        await displayMarketSummary();
        
    } catch (error) {
        console.error('Failed to initialize API:', error);
        // Show error message to user
        showErrorMessage('Failed to connect to server. Please check if the backend is running.');
    }
});

function showErrorMessage(message) {
    // Create and show error message
    const errorDiv = document.createElement('div');
    errorDiv.className = 'fixed top-4 right-4 bg-red-600 text-white p-4 rounded shadow-lg';
    errorDiv.textContent = message;
    document.body.appendChild(errorDiv);
    
    // Remove after 5 seconds
    setTimeout(() => {
        errorDiv.remove();
    }, 5000);
}

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { StockVisionAPI, api };
} 