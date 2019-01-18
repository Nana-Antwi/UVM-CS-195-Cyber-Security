#Nana Antwi 
#Assignment 2
#cs 195
##buffer overflow program with and exception

#import statements
import os 

##define main function
def main():
	try: 
		##set list size
		numList = [] * 8

		sumNum = 0
		counter = 0

		print("This program allows you to create a username with 8 numbers it shows buffer overflow if its more than25 character")
		print("welcome to the program")

		count = int(input("Enter the number the number 8! "))
		for i in range (0, count):
			numInput = int(input("Please enter each unique number followed by enter:"))
			numList[i]= numInput
			sumNum += numInput
			counter += 1

		print("\n Username created  ", numList)
		print("\n")

	except ValueError:
		return("Wrong Input")


main()
