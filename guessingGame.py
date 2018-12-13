import random

secretNum = random.randint(0, 1000)

num = int(input("Enter a number: "))
chances = 0

while (num != secretNum):
	if(num > secretNum):
		print("Too High!")
	elif(num < secretNum):
		print("Too Low!")
	num = int(input("Guess a number: "))
	chances += 1

print("You Win! " + "only " + str(chances) + " tries")