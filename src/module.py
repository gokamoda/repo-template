from src.mylogger import init_logging

LOG_PATH = "latest.log"
logger = init_logging(__name__, log_path=LOG_PATH)


def module_function():
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")