#TEST 2 LOG IN

#IMPORT STATEMENTS
import hashlib

def main():

	database={'name': '1234', 'name2': '5678', 'name3': '9012'}
	encrypted = dict([(name, hashlib.md5(pw).hexdigest()) for name, pw in database.items()])

	name = raw_input('Enter username: ')
	ask = raw_input('Enter pin: ')

	if name not in encrypted \
	      or hashlib.md5(ask).hexdigest() != encrypted.get(name):
	   raise ValueError("Username or password incorrect")
	else:
	   print("Welcome %s" % name)

main()