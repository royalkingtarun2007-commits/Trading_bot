def validate_order_input(symbol: str, side: str, order_type: str, quantity: float, price: float | None):
    symbol = symbol.upper().strip()
    if not symbol or not symbol.endswith("USDT"):
        raise ValueError("Symbol must be a USDT-M futures pair (e.g., BTCUSDT)")

    side = side.upper().strip()
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    order_type = order_type.upper().strip()
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    if order_type == "LIMIT":
        if price is None or price <= 0:
            raise ValueError("Price is required and must be > 0 for LIMIT orders")

    return symbol, side, order_type, quantity, price