import requests
from plyer import notification
from time import sleep

while True:

    try:
        data = requests.get("https://api.adviceslip.com/advice")

        data = data.json()

        advice = data["slip"]["advice"]

        notification.notify(
                title="Adivce",
                app_name="Advice",
                message=advice,
                app_icon="advice.ico"
            )


    except requests.exceptions.RequestException as e:
            pass
    
    sleep(7200)