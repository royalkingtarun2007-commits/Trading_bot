import logging

def setup_logging(log_file: str = "trading_bot.log"):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler()
        ],
        force=True
    )
    logging.getLogger("urllib3").setLevel(logging.WARNING)