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

try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token not available!"

if __name__ == "__main__":
    logger.info(f"Token value: {SOME_SECRET}")

    url = "https://sandbox.api.mailtrap.io/api/send/3034355"
    headers = {
        "Authorization": "Bearer 60258dfa6c4d18a7f92b3108cd33d5aa",
        "Content-Type": "application/json"
    }
    data = {
        "from": {
            "email": "mailtrap@example.com",
            "name": "Mailtrap Test"
        },
        "to": [
            {
                "email": "nasiri.aliabdullah@gmail.com"
            }
        ],
        "subject": "You are awesome!",
        "text": "Congrats for sending test email with Mailtrap!",
        "category": "Integration Test"
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    print(response.status_code)
    print(response.json())
