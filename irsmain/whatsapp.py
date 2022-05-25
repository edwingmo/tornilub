"""import requests, pyautogui, webbrowser
from time import sleep
from accounts.models import User

def whatsapp_welcome(phone_number):
    url = f'https://api.whatsapp.com/send?phone=58{User.phone_number}'

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("conectado al whatsapp")
            webbrowser.open(url)
            sleep(10)

            pyautogui.write("Gracias por registrarte en Tornilub")
            pyautogui.press("enter")
        else:
            print("no existe el telefono")
    except:
        pass"""