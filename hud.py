import tkinter as tk
from tkinter import ttk
import time

def update_labels(x4: list, x2: list, x05: list, x025: list, x0: list):
	global types_4, types_2, types_0_5, types_0_25, types_0, root
	types_4.config(text=str(x4))
	types_2.config(text=str(x2))
	types_0_5.config(text=str(x05))
	types_0_25.config(text=str(x025))
	types_0.config(text=str(x0))
	root.update()

root = tk.Tk()
frm = ttk.Frame(root, padding=10, )
frm.grid()

def exit_button_func():
	global root
	root.mainloop()
	root.destroy()

label_4 = ttk.Label(frm, text="4x", justify="left")
label_4.grid(row=0, column=0)
types_4 = ttk.Label(frm, text="", justify="left")
types_4.grid(row=0, column=1)

label_2 = ttk.Label(frm, text="2x", justify="left")
label_2.grid(row=1, column=0)
types_2 = ttk.Label(frm, text="", justify="left")
types_2.grid(row=1, column=1)

label_0_5 = ttk.Label(frm, text="0.5x", justify="left")
label_0_5.grid(row=2, column=0)
types_0_5 = ttk.Label(frm, text="", justify="left")
types_0_5.grid(row=2, column=1)

label_0_25 = ttk.Label(frm, text="0.25x", justify="left")
label_0_25.grid(row=3, column=0)
types_0_25 = ttk.Label(frm, text="", justify="left")
types_0_25.grid(row=3, column=1)

label_0 = ttk.Label(frm, text="0x", justify="left")
label_0.grid(row=4, column=0)
types_0 = ttk.Label(frm, text="", justify="left")
types_0.grid(row=4, column=1)

root.minsize(280, 200)

root.update()

# exit_button = ttk.Button(frm, text="Exit", command=exit_button_func)
# exit_button.grid(row=5, column=0, columnspan=2)
# not working under current approach