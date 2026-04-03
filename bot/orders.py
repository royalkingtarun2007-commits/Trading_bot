import logging
from .client import BinanceFuturesClient

logger = logging.getLogger(__name__)


def place_order(client: BinanceFuturesClient, symbol: str, side: str, order_type: str, quantity: float, price: float | None = None):
    """Business logic layer - can be extended later (e.g. position checks, TWAP, etc.)"""
    return client.place_order(symbol, side, order_type, quantity, price)