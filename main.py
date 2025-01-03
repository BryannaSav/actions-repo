import logging
import logging.handlers
import os

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

if __name__ == "__main__":
    r = requests.get('https://api.weather.gov/gridpoints/SEW/101,45/forecast')
    if r.status_code == 200:
        data = r.json()
        temperature = data["properties"]["periods"][0]["temperature"]
        logger.info(f'Weather in Olympia: {temperature}')