import argparse
import os
import logging
from bot.logging_config import setup_logging
from bot.validators import validate_order_input
from bot.orders import place_order
from bot.client import BinanceFuturesClient


def main():
    setup_logging()
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description="🚀 Binance Futures Testnet Trading Bot")
    parser.add_argument("--symbol", required=True, help="e.g. BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="BUY or SELL")
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"], help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, type=float, help="Quantity (e.g. 0.001)")
    parser.add_argument("--price", type=float, default=None, help="Price (required for LIMIT)")

    args = parser.parse_args()

    try:
        symbol, side, order_type, quantity, price = validate_order_input(
            args.symbol, args.side, args.type, args.quantity, args.price
        )

        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")
        if not api_key or not api_secret:
            raise ValueError("Please set BINANCE_API_KEY and BINANCE_API_SECRET environment variables")

        client = BinanceFuturesClient(api_key, api_secret)
        order = place_order(client, symbol, side, order_type, quantity, price)

        # === Clean Output ===
        print("\n" + "="*50)
        print("📋 ORDER REQUEST SUMMARY")
        print("="*50)
        print(f"Symbol     : {symbol}")
        print(f"Side       : {side}")
        print(f"Type       : {order_type}")
        print(f"Quantity   : {quantity}")
        if order_type == "LIMIT":
            print(f"Price      : {price}")
        print("="*50)
        print("✅ ORDER RESPONSE")
        print("="*50)
        print(f"Order ID       : {order.get('orderId')}")
        print(f"Status         : {order.get('status')}")
        print(f"Executed Qty   : {order.get('executedQty')}")
        print(f"Avg Price      : {order.get('avgPrice') or 'N/A'}")
        print(f"Cum Quote      : {order.get('cumQuote') or 'N/A'}")
        print("="*50)
        print("🎉 Order placed successfully on Binance Futures Testnet!")

    except ValueError as e:
        print(f"❌ Validation Error: {e}")
        logger.error(f"Validation failed: {e}")
    except Exception as e:
        print(f"❌ Failed to place order: {e}")
        logger.error(f"Order placement failed: {e}")


if __name__ == "__main__":
    main()