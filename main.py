import urllib3

from hamster import Hamster
from tokens import tokens
from function import send_email


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

for token in tokens:
    hamster = Hamster(token)
    data = hamster.collect_passive_earn()

    string = ""
    for key, value in data.items():
        string += f"{key}: {value}\n"

    string += "\n\n\n"

    send_email("Hamster Kombat", string)
