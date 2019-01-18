##Nana Antwi
##Assignment 7

##import statement
import os
import hashlib
import uuid

##main function
def main():


	def hash_password(password):
	    # uuid is used to generate a random number
	    salt = uuid.uuid4().hex
	    return hashlib.sha512(salt.encode() + password.encode()).hexdigest() + ':' + salt
	    
	def check_password(hashed_password, user_password):
	    password, salt = hashed_password.split(':')
	    return password == hashlib.sha512(salt.encode() + user_password.encode()).hexdigest()
	 
	new_pass = input('Please enter a password: ')
	hashed_password = hash_password(new_pass)
	print('The string is hashed and stored in the database: ' + hashed_password)
	old_pass = input('Re enter password to verify: ')
	if check_password(hashed_password, old_pass):
	    print('Your password is correct!!!')
	else:
	    print( 'Password does not match the one on file!')

main()