import re
from pyautogui import screenshot
from PIL import Image, ImageFilter
import pytesseract
import time
from difflib import get_close_matches
import pandas as pd

import CONFIG as cfg
from list import de_list, en_list
import weakness_calc as w

pokemon_types = pd.read_csv("p_types.csv")

def make_screenshot(region = cfg.SCR_REGION):
	'''
	Macht ein Screenshot der angegebenen `region` und speichert es als "screenshot.png".
	`region` ist ein Tupel der Form (left, top, width, height).
	Schließlich wird ein Gaußscher Weichzeichner angewendet und das Ergebnis als "scr_ed.png" gespeichert.
	'''
	scr = screenshot("screenshot.png", region=region)
	scr_ed = scr.filter(ImageFilter.GaussianBlur(1))
	scr_ed.save("scr_ed.png")

def ocr_image(image: Image.Image):
	'''
	Führt Tesseract OCR auf `image` durch und gibt den erkannten Text zurück.
	'''
	found_text = pytesseract.image_to_string(image)
	if not found_text:
		return None
	# print(found_text)
	return found_text

def clean_text(found_text: str):
	'''
	`found_text` wird bereinigt, indem alle nicht-alphabetischen Zeichen entfernt und in Kleinbuchstaben umgewandelt werden.
	'''
	cleaned_text = re.sub(r'[^a-zA-Z]+', '', found_text).lower()
	# print(cleaned_text)
	return cleaned_text

def translate(name: str):
	'''
	Übersetzt Pokemon-Name `name` ins englische, sofern die Spracheinstellung in `cfg.LANGUAGE` nicht "en" ist.
	'''
	if cfg.LANGUAGE != "en":
		translation = en_list[de_list.index(name)]
		return translation
	return name

def find_pokemon(cleaned_text: str):
	'''
	Findet den am besten passenden Pokemon-Namen in `en_list` für den bereinigten Text `cleaned_text`.
	'''
	closest_match = get_close_matches(cleaned_text, de_list, 1, 0)[0]
	# print("closest Match: " + closest_match)
	return closest_match

def get_types(pokemon_en: str):
	'''
	Gibt die Typen des Pokemons mit dem englischen Namen aus `p_types.csv` zurück.
	'''
	row = pokemon_types[pokemon_types['name'] == pokemon_en]
	types = [row.type1, row.type2]
	types = [t.values[0] for t in types if pd.notna(t.values[0])]
	return types

def get_weakness(types: list):
	'''
	Gibt die Schwächen des Pokemons basierend auf seinen `types` zurück.
	'''
	if len(types) == 2:
		return w.get_type_dict(types[0], types[1])
	else:
		return w.get_type_dict(types[0])

def get_lists_by_effectiveness(weakness: dict):
	x4 = w.get_keys_by_value(weakness, 4.0)
	x2 = w.get_keys_by_value(weakness, 2.0)
	xhalf = w.get_keys_by_value(weakness, 0.5)
	xquart = w.get_keys_by_value(weakness, 0.25)
	xnone = w.get_keys_by_value(weakness, 0.0)
	return [x4, x2, xhalf, xquart, xnone]

def main():
	make_screenshot()
	text = ocr_image(Image.open("scr_ed.png"))
	if not text:
		return
	cleaned_text = clean_text(text)
	pokemon_de = find_pokemon(cleaned_text)
	if not cleaned_text:
		return
	try:
		pokemon_en = translate(pokemon_de)
		pokemon_en = find_pokemon(pokemon_en)
	except (ValueError, IndexError):
		print("Pokémon nicht gefunden.", cleaned_text, pokemon_de)
		return
	types = get_types(pokemon_en)
	weakness = get_weakness(types)
	weakness = w.convert_num_to_type(weakness)
	effectiveness_lists = get_lists_by_effectiveness(weakness)
	print(f"Pokémon: {pokemon_de}, Typen: {types}")
	print("4x:", effectiveness_lists[0])
	print("2x:", effectiveness_lists[1])
	print("½x:", effectiveness_lists[2])
	print("¼x:", effectiveness_lists[3])
	print("0x:", effectiveness_lists[4])
	return

if __name__ == "__main__":
	while True:
		main()
		time.sleep(10)