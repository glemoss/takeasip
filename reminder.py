import time
import os

from dotenv import load_dotenv
from mac_notifications import client


if __name__ == "__main__":
    load_dotenv()

    while True:
        if time.time() % 1800 == 0:
            client.create_notification(
            title="Water Reminder!",
            subtitle="Take a sip now!",
            icon=os.environ["CAMINHO_IMAGEM"],
            action_button_str="Drink",
)