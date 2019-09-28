import logging

log_format = "%(asctime)s:%(levelname)s:%(filename)s: %(message)s"
logging.basicConfig(level=logging.DEBUG,
                    #filename="app.log",
                    format=log_format,
                    handlers=[
                        logging.StreamHandler(),
                        logging.FileHandler("app.log")
                    ])

logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")

try:
    x = 0
    y = 1 / x
except Exception as exc:
    logging.critical(exc, exc_info=True)
