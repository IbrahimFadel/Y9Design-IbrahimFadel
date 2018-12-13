
#Import all contents of tkinter for the gui
from tkinter import *

# Tk() makes a window
window = Tk()

def return_entry(en):
	content = entry.get()
	if(content != ""):
		print(content)

	entry.delete(0, END)

Label(window, text="Input: ").grid(row=0)

entry = Entry(window)
entry.grid(row=0, column=1)
entry.bind('<Return>', return_entry)

#keep window open
mainloop()