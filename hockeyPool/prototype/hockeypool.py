#import tkinter and pillow
from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import messagebox
from bs4 import BeautifulSoup
import requests
from tkinter import filedialog


#savedData = savedData.replace('[', "")
#savedData = savedData.replace(']', "")
#players.append(savedData)
#print(savedData)
#players = players.replace('"', "")

site = requests.get('http://www.hockey-reference.com/leagues/NHL_2019_skaters.html')
if site.status_code is 200:   
		content = BeautifulSoup(site.content, 'html.parser')  
else:
	content = -99

def switchPhoto():
	global photo
	my_image = Image.open("headshots/kesseph01.jpg")
	photo = ImageTk.PhotoImage(my_image)
	canvas.itemconfig(my)

def makeOptionsList():
	if content != -99:
		names = content.findAll(attrs={"data-stat": "player"})
		playerOptions = []
		for player in names:
			if(player != "None"):
				playerOptions.append(player.get('csk'))
		return playerOptions

def deletePlayer():
	items = playerList.curselection()
	pos = 0
	for i in items:
		idx = int(i) - pos
		playerList.delete( idx,idx )
		pos = pos + 1

#When a player name is selected, display these labels/buttons
def onSelect(evt):
	global photo
	global image1
	title = Label(root, text="Player Info: ")
	title.place(x=250, y=125)

	myplayer = playerList.get(ANCHOR)
	dTag = content.find(attrs={"csk": myplayer})
	parent = dTag.findParent('tr')
	pts = parent.contents[8].text
	plusMinus = parent.contents[9].text
	penMins = parent.contents[10].text
	hits = parent.contents[24].text
	age = parent.contents[2].text
	team = parent.contents[3].text
	pos = parent.contents[4].text

	ageLabel = Label(root, text="Age: " + age + " ")
	ageLabel.place(x=250, y=145)

	pointsLabel = Label(root, text="PTS: " + pts + " ")
	pointsLabel.place(x=250, y=165)

	plusMinusLabel = Label(root, text="+/- " + plusMinus + " ")
	plusMinusLabel.place(x=250, y=185)

	penaltyMinutesLabel = Label(root, text="Penalty Minutes: " + penMins + " minutes ") 
	penaltyMinutesLabel.place(x=250, y=205)

	teamLabel = Label(root, text="Team: " + team + " ")
	teamLabel.place(x=250, y=225)

	posLabel = Label(root, text="Position: " + pos + " ")
	posLabel.place(x=250, y=245)

	deletePlayerButton = Button(root, text="Delete Player from List", command=deletePlayer)
	deletePlayerButton.place(x=400, y=150)

	ageLabel.configure(text="Age: " + age + " ")
	pointsLabel.configure(text="PTS: " + pts + " ")
	plusMinusLabel.configure(text="+/- " + plusMinus + " ")
	penaltyMinutesLabel.configure(text="Penalty Minutes: " + penMins + " minutes ")
	teamLabel.configure(text="Team: " + team + " ")
	posLabel.configure(text="Position: " + pos + " ")

	file = str(myplayer)
	a,b = file.split(",")

	if a.count(".") > 0:
		aOne,aTwo = a.split(".")
		print(aOne, aTwo)
	elif b.count(".") > 0:
		bOne,bTwo = b.split(".")
		print(bOne, bTwo)


	file = a[0:5].lower() + b[0:2].lower() + "01"
	test = "headshots/" + file + ".jpg"
	print(test)
	image1 = Image.open(test)
	photo = ImageTk.PhotoImage(image1)

	canvas.create_image(470, 200, anchor=NW, image=photo)


def helpWindow():
	helpWindow = Tk()
	helpWindow.geometry("300x300+700+0")
	helpWindow.title("Help")

	titleLabel = Label(helpWindow, text="Help/Instructions")
	titleLabel.place(x=83, y=15)

	helpLabel = Label(helpWindow, text=helpMessage)
	helpLabel.place(x=10, y=40)

	helpWindow.mainloop()

def scrape():
	# 8  is pts
	# 9 is +/-
	# 10 is penalty minutes
	# 24 is hits

	length = len(stats)
	index = 0

	if stats.count("PTS") > 0:
		index += 1
	if stats.count("+/-") > 0:
		index += 1
	if stats.count("Penalty Minutes") > 0:
		index += 1
	if stats.count("Hits") > 0:
		index += 1

	if (messagebox.askyesno("Wait?", "This could take a few seconds. Wait?") == False):
		return
	totalpts = 0
	for myplayer in players: # loop to check my players
		dTag = content.find(attrs={"csk": myplayer})
		parent = dTag.findParent('tr')
		if stats.count("Age") > 0:
			playerAge = int(parent.contents[2].text)
		else:
			playerAge = "Not Tracked"
		if stats.count("PTS") > 0:
			playerpts = int(parent.contents[8].text)
			totalpts += playerpts
		else:
			playerpts = "Not Tracked"
		if stats.count("+/-") > 0:
			playerPlusMinus = int(parent.contents[9].text)
			totalpts += playerPlusMinus
		else:
			playerPlusMinus = "Not Tracked"
		if stats.count("Penalty Minutes") > 0:
			playerPenMins = int(parent.contents[10].text)
			totalpts += playerPenMins
		else:
			playerPenMins = "Not Tracked"
		if stats.count("Hits") > 0:
			playerHits = int(parent.contents[24].text)
			totalpts += playerHits
		else:
			playerHits = "Not Tracked"
		if stats.count("Team") > 0:
			playerTeam = parent.contents[3].text
		else:
			playerTeam = "Not Tracked"
		if stats.count("Position") > 0:
			playerPos = parent.contents[4].text
		else: 
			playerPos = "Not Tracked"

	dataWindow = Tk()
	dataWindow.geometry("500x500+0+0")
	dataWindow.title("Hockey Pool")
	dataWindow.configure(background="white")

	title = Label(dataWindow, text="Final Info")
	title.place(x=220, y=30)

	pointsLabel = Label(dataWindow, text="Points Sum")
	pointsLabel.place(x=60, y=120)

	points = Label(dataWindow, text=playerpts)
	points.place(x=150, y=120)

	plusLabel = Label(dataWindow, text="+/- Sum")
	plusLabel.place(x=60, y=160)

	plus = Label(dataWindow, text=playerPlusMinus)
	plus.place(x=150, y=160)

	ppmLabel = Label(dataWindow, text="Penalty Minutes")
	ppmLabel.place(x=60, y=200)

	ppm = Label(dataWindow, text=playerPenMins)
	ppm.place(x=180, y=200)

	hitsLabel = Label(dataWindow, text="Hits")
	hitsLabel.place(x=60, y=240)

	hits = Label(dataWindow, text=playerHits)
	hits.place(x=150, y=240)

	dataWindow.mainloop()

def addPlayer():
	#print(variable.get())
	global players
	name = variable.get()
	#print(players)
	if name == "None":
		messagebox.showinfo("Error", "Select a player! Not an empty option")
		return
	if players.count(name) > 0:
		messagebox.showinfo("Error", "Player already in the list")
		return
	playerList.insert(END, name)
	#for i in range(playerList.size()):
	players.append(name)

def addStat():
	global stats
	stat = var.get()
	if(stats.count(stat) > 0):
		messagebox.showinfo("Error", "Stat already in the list")
		return
	stats.append(stat)
	statsList.insert(END, stat)

def save():
	#print(players)
	global players
	f = open("hockeyPool.txt", "w")
	for player in players:
		f.write(player + ".")
	#f.write(str(players))
	f.close()
	messagebox.showinfo("hockeyPool.txt", "Players saved to disk")

def saveAs():
	f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
	t = str(players)
	f.write(t.rstrip())

#Create the window, set the size/position, title and background
root = Tk()
root.geometry("1500x700+0+0")
root.title("Hockey Pool")
root.configure(background="white")

#print("Downloading Hockey Data")
players = []
lst = []
totalpts = 0


stats = []
statsSelected = []
#statsSelected = []

helpMessage = "Select a player in the list to find it's \n stats. To add another player \n to the list, select it in the  \n option menu. Next, select which stats \n you would like \n to get a total of, \n Finally, press the find total stats button, \n and Voila!"


#Create the canvas, PARAMS: window, width, height, background
canvas = Canvas(root, width = 1500, height = 700, bg = 'white')
canvas.grid(row=0, column=0, padx=0, pady=5)

image1 = Image.open('headshots/armiajo01.jpg')
image1.putalpha(1)
photo = ImageTk.PhotoImage(image1)
canvas.create_image(0, 0, anchor=NW, image=photo)

#Create the backgorund image(P.K Subban), and enlarge it to fit the screen
#Then put alpha to decrease it's opacity
background = Image.open("background.png").resize((1420, 695), Image.ANTIALIAS)
background.putalpha(68)
backgroundImage = ImageTk.PhotoImage(background)
canvas.create_image(0, 0, anchor=NW, image=backgroundImage)

#Make the hockey puck graphic PARAMS: x1, y1, x2, y2, fill, outline, width
graphic = canvas.create_oval(25, 25, 125, 125, fill="black", outline="#DDD", width=4)
graphicText = canvas.create_text(75, 75, text="Hockey Pool", fill="white")
graphicTitle = canvas.create_text(260, 80, text="HOCKEY POOL")

playerListLabel = Label(root, text="List of Players Currently Selected")
playerListLabel.place(x=5, y=160)

#Create the list of players PARAMS: window, height
playerList = Listbox(root, height=7)
playerList.place(x=20, y=180)

playerList.bind("<<ListboxSelect>>", onSelect)

f = open("hockeyPool.txt", "r")
savedData = f.read()
savedData = savedData.split('.')
savedData = list(savedData)
for i in range(len(savedData) - 1):
	players.append(savedData[i])
	playerList.insert(END, savedData[i])
print(players)

#List of players to be options in our option menu
OPTIONS = makeOptionsList()
variable = StringVar(root)
variable.set("None")

#Create an option menu PARAMS:window, var, and list of strings
playerOptionMenu = OptionMenu(root, variable, *OPTIONS)
playerOptionMenu.place(x=20, y=310)

addPlayerButton = Button(root, text="Add player", command=addPlayer)
addPlayerButton.place(x=170, y=310)


helpButton = Button(root, text="Help", command=helpWindow)
helpButton.place(x=360, y=75)

statsListLabel = Label(root, text="List of stats that will be added up in your total")
statsListLabel.place(x=5, y=370)

statsList = Listbox(root, height=5)
statsList.place(x=20, y=400)

STATSOPTIONS = ["PTS", "+/-", "Penalty Minutes", "Hits"]
var = StringVar()
statsOptions = OptionMenu(root, var, *STATSOPTIONS)
statsOptions.place(x=20, y=490)

addStatButton = Button(root, text="Add Stat", command=addStat)
addStatButton.place(x=170, y=490)

totalStatsButton = Button(root, text="Find Total Stats Value", command=scrape)
totalStatsButton.place(x=20, y=530)

saveButton = Button(root, text="Save", command=save)
saveButton.place(x=300, y=530)

saveAsButton = Button(root, text="Save As", command=saveAs)
saveAsButton.place(x=350, y=530)

#Keep the window open
root.mainloop()