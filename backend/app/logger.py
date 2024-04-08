import logging
import sys

from app.core.config import BASE_DIR

logger = logging.getLogger()

log_format = "%(asctime)s - %(levelname)s - %(message)s"
formatter = logging.Formatter(log_format)

stream_handler = logging.StreamHandler(sys.stdout)
path_to_log_file = BASE_DIR / "logs" / "logs.txt"
file_handler = logging.FileHandler(path_to_log_file)

stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.handlers = [stream_handler, file_handler]

logger.setLevel(logging.INFO)
