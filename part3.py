#Nana Antwi
#CS 195 
#Assigmnent 6
#part 3

#import statements
import os
import hashlib

#defn variables 
hash_decrypt = "cc8b1415557f58abf2e2fa83c2ea6c91"
my_file = "wordlist800.txt"

#main function
def main():

	#open and read wordslsit 800
    with open(my_file) as fileobject:
        for line in fileobject:
            line = line.strip()
            if hashlib.md5(line.encode("utf-8")).hexdigest() == hash_decrypt:
                print ("Successfully decrypt the hash %s: It's %s" % (hash_decrypt, line))
                return ""
    print("Failed to decrypt hash password")

if __name__ == "__main__":
    main()
