import time
import os

from dotenv import load_dotenv
from mac_notifications import client


if __name__ == "__main__":
    load_dotenv()

    image_path=''
    seconds = 1800

    while True:
        if time.time() % seconds == 0:
            client.create_notification(
            title="Water Reminder",
            subtitle="Take a sip now!",
            icon=os.environ[image_path],
            action_button_str="Drink",
)