import time

from mac_notifications import client


if __name__ == "__main__":
    image_path='/Users/glemoss/Workspace/python/water-reminder/assets/logo.png'
    seconds = 1800

    while True:
        if time.time() % seconds == 0:
            client.create_notification(
            title="Water Reminder",
            subtitle="Take a sip now!",
            icon=image_path,
            action_button_str="Drink",
)