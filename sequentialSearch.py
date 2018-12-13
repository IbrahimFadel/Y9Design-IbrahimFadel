# get input and convert it to int right away for later use
num = int(input("Enter a number: "))
myList = [1, 2, 3, 4, 5]
for i in myList:
	if i == num:
		if i == 1:
			print("Your number: " + str(num) + " was found in the list under the index of: 0")
			break
		else:
			print("Your number: " + str(num) + " was found in the list under the index of: " + str(myList[i - 2]))
			break
	else:
		print("Your number: " + str(num) + " is not " + str(i))