#import tkinter, messagebox, beautiful soup, and requedts
from tkinter import *
from tkinter import messagebox
from bs4 import BeautifulSoup
import requests
import tkFileDialog

# update the list
def updatelab():
	lstprint = ""
	for item in lst:
		lstprint = lstprint + item + "\n"
	mylab.configure(text=lstprint)

# add a player to the list 
def addItem():
	item = entry.get()
	if lst.count(item) == 0:
		lst.append(item)
		entry.delete(0, END)
		updatelab()


# delete an item from the list
def deleteItem():
	item = entry.get()
	if lst.count(item) > 0:
		lst.remove(item)
		entry.delete(0, END)
		updatelab()

# saves file
def saveFile():
	"""f = open("hockeyPool.txt", "w")
	f.write(str(lst))
	f.close()"""
	f = open("hockeyPool.txt", "w")
	for player in lst:
		f.write(player + "\n")
	f.close()
	messagebox.showinfo("hockeyPool.txt", "Players saved to disk")

# "save as" the file, you can chose the name
def saveAs():
	fileName = str(input("What is the name of your file?"))
	#fileName = messagebox.askquestion("What is the name of your file?")
	f = open(fileName, "x")
	for player in lst:
		f.write(player + "\n")

def scrape():
	if (messagebox.askyesno("Wait?", "This could take a few seconds. Wait?") == False):
		return
	if site.status_code:
		content = BeautifulSoup(site.content, 'html.parser')                    
		totalpts = 0
		dTag = content.find(attrs={"csk": myplayer})
		if dTag is None:
			print(myplayer + " not found")
		else:
			for myplayer in lst: # loop to check my players
				parent = dTag.findParent('tr')
				playerpts = int(parent.contents[8].text) # 8th tag is total points
				print(myplayer + " " + str(playerpts))
				totalpts = totalpts + playerpts         
			mypts.configure(text=totalpts)

#declare global variables
lst = []
lstprint = ""
totalpts = 0
site = requests.get('http://www.hockey-reference.com/leagues/NHL_2019_skaters.html')
print("Downloading Hockey Data")

#create the tkinter window
root = Tk()
root.geometry("300x400+0+900")
root.title("Hockey Pool")

instlab = Label(root, text="Input (eg. McDavid,Connor): ")
instlab.grid(row=0, column=2)

entry = Entry(root)
#entry.pack()
entry.grid(row=1, column=2)

addbutton = Button(root, text="Add", command=addItem)
addbutton.grid(row=3, column=0)
#addbutton.pack()


deletebutton = Button(root, text="Delete", command=deleteItem)
deletebutton.grid(row=4, column=0)
#deletebutton.pack()


saveButton = Button(root, text="Save", command=saveFile)
saveButton.grid(row=5, column=0)
#saveButton.pack()


saveAsButton = Button(root, text="Save As", command=saveAs)
saveAsButton.grid(row=6, column=0)
#saveAsButton.pack()

mylab = Label(root, text=lstprint, anchor=W, justify=CENTER)
mylab.grid(row=2, column=2)

ptsButton = Button(root, text="Find Total Points?", command=scrape)
ptsButton.grid(row=8, column=2)

mypts = Label(root, text=totalpts)
mypts.grid(row=9, column=2)


# ADD ALL LABELS BUTTONS ENTRIES ^^^^^^^^^^^^^^^^^^^

"""soup = BeautifulSoup(site.content, 'html.parser')
data = soup.find('th', class_=' poptip sort_col center')
dataPoints = list(data.children)
actualData = dataPoints[0]

pts = list(soup.find_all('td', class_='right'))
childresOne = pts[3]
hiThere = list(childresOne.children)
print(hiThere)"""

#keep the window open
mainloop()