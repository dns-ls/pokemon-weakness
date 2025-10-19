import pandas as pd

type_map = {
	0: "normal", 1: "feuer", 2: "wasser", 3: "elektro", 4: "pflanze",
	5: "eis", 6: "kampf", 7: "gift", 8: "boden", 9: "flug",
	10: "psycho", 11: "käfer", 12: "gestein", 13: "geist", 14: "drache",
	15: "unlicht", 16: "stahl", 17: "fee"
}

table = pd.read_csv("type_weaknesses.csv")

def get_type_dict(type1: str, type2: str = "None"):
	if type2 == "None":
		return table[type1].astype(float).to_dict()
	else:
		return (table[type1] * table[type2]).astype(float).to_dict()

def get_keys_by_value(di: dict, value: float):
	return [k for k, v in di.items() if v == value]

def convert_num_to_type(di: dict):
	return {type_map.get(int(k), k): v for k, v in di.items()}