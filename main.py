import re
from pyautogui import screenshot
from PIL import Image, ImageFilter
import pytesseract
import os
from difflib import get_close_matches
import pandas as pd

import CONFIG as cfg
from list import de_list, en_list
from model import singleWeakness

pokemon_types = pd.read_csv("p_types.csv")

def make_screenshot(region = cfg.SCR_REGION):
	scr = screenshot("screenshot.png", region=region)
	scr_ed = scr.filter(ImageFilter.GaussianBlur(1))
	scr_ed.save("scr_ed.png")

def ocr_image(image: Image.Image):
	found_text = pytesseract.image_to_string(image)
	if not found_text:
		return None
	# print(found_text)
	return found_text

def clean_text(found_text: str):
	cleaned_text = re.sub(r'[^a-zA-Z]+', '', found_text).lower()
	# print(cleaned_text)
	return cleaned_text

def translate(name: str):
	if cfg.LANGUAGE != "en":
		pokedex_index = de_list.index(name)
		translation = en_list[pokedex_index]
		return translation
	return name

def find_pokemon(cleaned_text: str):
	closest_match = get_close_matches(cleaned_text, en_list, 1, 0)[0]
	# print("closest Match: " + closest_match)
	return closest_match

def get_types(pokemon_en: str):
	row = pokemon_types[pokemon_types['name'] == pokemon_en]
	types = [row.type_1, row.type_2]
	types = [t.values[0] for t in types if pd.notna(t.values[0])]
	return types

def get_weakness(types: list):
	if len(types) == 2:
		return singleWeakness(types[0], types[1])
	else:
		return singleWeakness(types[0])