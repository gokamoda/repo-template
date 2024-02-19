import logging
import sys
from pathlib import Path


def init_logging(logger_name: str, log_path: str = "logs/info.log") -> logging.Logger:
    """_summary_

    Parameters
    ----------
    logger_name : str
        _description_
    log_path : str, optional
        _description_, by default "logs/info.log"

    Returns
    -------
    logging.Logger
        _description_
    """

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    path = Path(log_path)

    dir_path = path.parent
    if not dir_path.exists():
        dir_path.mkdir(parents=True)

    if logger.handlers == []:
        dir_path.mkdir(parents=True, exist_ok=True)
        formatter = logging.Formatter("%(asctime)s/%(levelname)s/%(name)s/%(funcName)s():%(lineno)s\n%(message)s \n")

        # file handler
        fh = logging.FileHandler(log_path)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)

        # console handler
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

        logger.propagate = False

    return logger


# if __name__ == "__main__":
#     mylogger = init_logging(__name__, log_dir="logs", filename="test_logger.log", reset=True)
#     mylogger.debug("debug")
#     mylogger.info("info")
#     mylogger.warning("warning")
#     mylogger.error("error")
#     mylogger.critical("critical")

#     mylogger2 = init_logging("second", log_dir="logs", filename="test_logger.log", reset=False)
#     mylogger2.debug("debug")
#     mylogger2.info("info")
#     mylogger2.warning("warning")
#     mylogger2.error("error")
#     mylogger2.critical("critical")
