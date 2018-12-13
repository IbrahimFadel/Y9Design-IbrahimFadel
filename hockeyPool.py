from tkinter import *

def updatelab():
	lstprint = ""
	for item in lst:
		lstprint = lstprint + item + "\n"
	mylab.configure(text=lstprint)

def addItem():
	item = entry.get()
	if lst.count != 0:
		lst.append(item)
		entry.delete(0, END)
		updatelab()

lst = []
lstprint = ""

root = Tk()
root.geometry("300x400+0+900")
root.title("Hockey Pool")

instlab = Label(root, text="Input (eg. McDavid,Connor): ")
instlab.pack()

entry = Entry(root)
entry.pack()

addbutton = Button(root, text="Add", command=addItem)
addbutton.pack()

mylab = Label(root, text=lstprint, anchor=W, justify=CENTER)
mylab.pack()

mainloop()