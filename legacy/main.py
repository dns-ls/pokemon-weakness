import re
import pyautogui
from PIL import Image, ImageFilter
import pytesseract
import os
import requests
from list import de_list, en_list
from model import singleWeakness
from time import sleep
from difflib import get_close_matches
pytesseract.pytesseract.tesseract_cmd = (
    "C:\\Program Files\\Tesseract-OCR\\tesseract.exe")

letztesPKM = ""


def bildmachen():
    scr = pyautogui.screenshot("scr.png", region=(0, 187, 329, 76))
    scr_ed = scr.filter(ImageFilter.GaussianBlur(1))
    scr_ed.save("scr_ed.png")
    gefunden = pytesseract.image_to_string(Image.open('scr_ed.png'))
    if not gefunden:
        return 0
    print(gefunden)
    os.remove("scr.png")
    return gefunden

def bereinigen(gefunden):
    #whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    gefundenBereinigt = re.sub(r'[^a-zA-Z]+', '', gefunden).lower()
    print("gef: " + gefundenBereinigt)
    closestMatch = get_close_matches(gefundenBereinigt, de_list, 1,0)[0]
    print("closest Match: " + closestMatch)
    global letztesPKM
    letztesPKM = closestMatch
    return closestMatch

def translate(name): 
    pokedex = de_list.index(name)
    translation = en_list[pokedex]
    print(translation)
    return (translation)

def get_types(pokemonEN):
    response = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokemonEN).json()
    data = str([e["type"]["name"] for e in response["types"]])
    data = re.sub(r'[^a-zA-Z ]+', '', data).lower()
    return data

def get_weakness(pokemon):
    try:
        type1, type2 = get_types(translate(pokemon)).split(' ', 1)
        return singleWeakness(type1, type2)
    except ValueError:
        return singleWeakness(get_types(translate(pokemon)))

'''    
def fenster():
    layout = [[sg.Text()], [sg.Button("OK")]]
    # Create the window
    window = sg.Window("asd", layout)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "OK" or event == sg.WIN_CLOSED:
            break
    window.close()
'''


while True:
    try:
        get_weakness(bereinigen(bildmachen()))
    except Exception:
        pass

    sleep(10)