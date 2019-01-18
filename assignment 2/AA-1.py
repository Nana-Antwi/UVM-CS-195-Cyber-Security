#Nana Antwi
#CS 195
#Assignment 2
#Buffer overflow program 

#import statements
import os 

##define main function
def main():
	 
		##define variables and set size of variables 
		numList = [] * 25

		sumNum = 0
		counter = 0

		print("This program allows enter a username bewtween 8-25 combination of numbers")
		print("Welcome! you will enter your username soon!")

		count = int(input("Select any combination you wish as username!"))
		for i in range (0, count):
			numInput = int(input("Please enter your username "))
			numList[i]= numInput
			sumNum += numInput
			counter += 1

		print("\n The username you chose was  ", numList)
		print("\n")

	

main()
