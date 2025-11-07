import tkinter as tk
from tkinter import ttk
import time

def update_labels(x4: list, x2: list, x05: list, x025: list, x0: list, name: str = "-", types: list = []):
	global types_4, types_2, types_0_5, types_0_25, types_0, label_name, label_types, root
	types_4.config(text=str(x4))
	types_2.config(text=str(x2))
	types_0_5.config(text=str(x05))
	types_0_25.config(text=str(x025))
	types_0.config(text=str(x0))
	name_text = name + ", " + str(types)
	label_name.config(text=name_text)
	root.update()

root = tk.Tk()
frm = ttk.Frame(root, padding=10, )
frm.grid()

def exit_button_func():
	global root
	root.mainloop()
	root.destroy()

label_name = ttk.Label(frm, text="-", anchor="w")
label_name.grid(row=0, column=0, sticky="w", columnspan=2)

label_4 = ttk.Label(frm, text="4x", anchor="w")
label_4.grid(row=1, column=0, sticky="w")
types_4 = ttk.Label(frm, text="", justify="left", anchor="w", wraplength=199)
types_4.grid(row=1, column=1, sticky = "w")

label_2 = ttk.Label(frm, text="2x", anchor="w")
label_2.grid(row=2, column=0, sticky="w")
types_2 = ttk.Label(frm, text="", justify="left", anchor="w", wraplength=199)
types_2.grid(row=2, column=1, sticky = "w")

label_0_5 = ttk.Label(frm, text="0.5x", anchor="w")
label_0_5.grid(row=3, column=0, sticky="w")
types_0_5 = ttk.Label(frm, text="", justify="left", anchor="w", wraplength=199)
types_0_5.grid(row=3, column=1, sticky = "w")

label_0_25 = ttk.Label(frm, text="0.25x", anchor="w")
label_0_25.grid(row=4, column=0, sticky="w")
types_0_25 = ttk.Label(frm, text="", justify="left", anchor="w", wraplength=199)
types_0_25.grid(row=4, column=1, sticky = "w")

label_0 = ttk.Label(frm, text="0x", anchor="w")
label_0.grid(row=5, column=0, sticky="w")
types_0 = ttk.Label(frm, text="", justify="left", anchor="w")
types_0.grid(row=5, column=1, sticky = "w")

root.minsize(200, 150)

root.update()

# exit_button = ttk.Button(frm, text="Exit", command=exit_button_func)
# exit_button.grid(row=5, column=0, columnspan=2)
# not working under current approach