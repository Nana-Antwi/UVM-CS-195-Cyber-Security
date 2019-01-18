#Nana Antwi
#CS 195 
#assignment 6.0
#part one

#import statements
import os 
import hashlib

def main():
	#define vairiable 
	password_1 = 'letMeIn'
	password_2 = 'admin'
	password_3 = 'gr8tPW'
	password_4 = 'hello123'
	password_5 = 'v@ry$ecURE!'

	#hash password
	hash_1 = hashlib.md5(password_1.encode("utf-8")).hexdigest()
	hash_2 = hashlib.md5(password_2.encode("utf-8")).hexdigest()
	hash_3 = hashlib.sha1(password_3.encode("utf-8")).hexdigest()
	hash_4 = hashlib.sha256(password_4.encode("utf-8")).hexdigest()
	hash_5 = hashlib.sha512(password_5.encode("utf-8")).hexdigest()


	print (hash_1)
	print (hash_2)
	print (hash_3)
	print (hash_4)
	print (hash_5)
main()

