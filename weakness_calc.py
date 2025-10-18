import pandas as pd

table = pd.read_csv("type_weaknesses.csv")

def get_type_effectiveness(type1: str, type2: str = "None"):
	if type2 == "None":
		return
	return table.loc[table['attacking_type'] == type1, type2].values[0]