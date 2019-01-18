##Nana Antwi
##assignment 5


##import statements
import os
import hashlib

##main function
def main():
	## sha256 hash
	hash_object = hashlib.sha256(b'test')
	hex_dig = hash_object.hexdigest()
	print(hex_dig)

	##sha 1 
	hash_object = hashlib.sha1(b'tset')
	hex_dig = hash_object.hexdigest()
	print(hex_dig)

	##input any string ti be hashed 
	mystring = input('Enter any string to hashed in md5: ')
	#default UTF-8
	hash_object = hashlib.md5(mystring.encode())
	print("Your hashed string")
	print(hash_object.hexdigest())

main()
