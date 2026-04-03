# Binance Futures Testnet Trading Bot

A lightweight Python-based trading bot that places Market and Limit orders on the Binance Futures Testnet (USDT-M).
Built with a focus on clean architecture, input validation, logging, and error handling.

---

## Features

* Place Market and Limit orders
* Supports both BUY and SELL
* CLI-based input using arguments
* Structured and modular codebase
* Robust error handling
* Logging of API requests, responses, and failures
* Works with Binance Futures Testnet (USDT-M)

---

## Tech Stack

* Python 3.x
* requests / python-binance (based on implementation)
* argparse (or Typer/Click if used)
* Python logging module

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│
├── cli.py
├── requirements.txt
├── README.md
├── logs/
│   ├── market_order.log
│   └── limit_order.log
```

---

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/yourusername/trading-bot.git
cd trading-bot
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Configure API Credentials

Create a `.env` file or update your configuration with:

```
API_KEY=your_api_key
API_SECRET=your_api_secret
BASE_URL=https://testnet.binancefuture.com
```

---

## How to Run

### Market Order Example

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

### Limit Order Example

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 65000
```

---

## Sample Output

```
Order Summary:
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

Response:
Order ID: 12345678
Status: FILLED
Executed Quantity: 0.001
Average Price: 66250.5

Status: SUCCESS
```

---

## Logging

* All API requests, responses, and errors are logged
* Logs are stored in the `logs/` directory
* Includes market and limit order execution logs

---

## Error Handling

The application handles:

* Invalid CLI inputs
* Missing parameters
* API errors (Binance response issues)
* Network failures

---

## Assumptions

* User has a valid Binance Futures Testnet account
* API credentials are correctly configured
* Testnet base URL is used

---

## Testnet Endpoint

```
https://testnet.binancefuture.com
```

---

## Notes

* This project is intended for testing and demonstration purposes
* No real funds are used
* Designed to showcase clean architecture and API integration

---

## Author

Tarun Nani

---

## Deliverables Covered

* Market and Limit order placement
* BUY and SELL support
* CLI-based execution
* Logging implementation
* Error handling
* Structured codebase
* Clear setup and usage instructions
