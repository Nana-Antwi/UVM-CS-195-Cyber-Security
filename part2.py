#Nana Antwi
#CS 195
#Assignment 6
#part 2

#import statements 
import hashlib
import os

#def main
def main():

	#def vairiables 
	password = 'helpdesk'
	salt = 'cyber'
	sugar = os.urandom(16)
	 
	m = hashlib.md5(salt + password.encode('utf-8')).hexdigest()
	m.update()
	print (m)
	

	s = hashlib.md5(sugar + salt + password.encode('utf-8')).hexdigest()
	s.update()
	print (s)
main()