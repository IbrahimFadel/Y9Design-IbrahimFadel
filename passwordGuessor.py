secret = "joe"

i = 0

while i < 3:
	pssWord = input("Enter a password: ")

	i += 1

	if(secret == pssWord):
		print("Welcome")
		break
	elif(i == 3):
		print("That's three incorrect answers... You've been locked out!")
	else:
		print("Incorrect... you have: " +str(3 - i) + " tries left")