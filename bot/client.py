import logging
from binance import Client
from binance.exceptions import BinanceAPIException

logger = logging.getLogger(__name__)


class BinanceFuturesClient:
    def __init__(self, api_key: str, api_secret: str):
        self.client = Client(api_key, api_secret, testnet=True)
        logger.info("Binance Futures Testnet client initialized (testnet=True)")

    def place_order(self, symbol: str, side: str, order_type: str, quantity: float, price: float | None = None):
        logger.info(f"Placing {side} {order_type} order | {quantity} {symbol} {'@ ' + str(price) if price else 'MARKET'}")

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT" and price is not None:
            params["price"] = price
            params["timeInForce"] = "GTC"

        try:
            order = self.client.futures_create_order(**params)
            logger.info(f"Order placed successfully | orderId={order.get('orderId')}")
            return order
        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise