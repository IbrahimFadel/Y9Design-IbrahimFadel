myInput = int(input("Enter a Number: "))

if(myInput < 100):
	print("Your Number, " + str(myInput) + ", is less than 100")
elif(myInput > 100):
	print("Your Number, " + str(myInput) + ", is greater than 100")
else:
	print("Your Number, " + str(myInput) + ", is equal to 100")