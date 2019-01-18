import os

#Must Access this to continue.
def main():
    while True:
        username = input ("Enter Username: ")
        password = input ("Enter Password: ")


        #open a file and save 
        myfile = open(UserInfo+".csv", "a")

        #wrtie user information to
        myfile.write("User log-in id"+username+"\n")
        myfile.write("User Password id:"+password+"\n")

        #close file
        myfile.close()

        #open and read information

        if UserName == 'Bob' and PassWord == 'rainbow123':
            time.sleep(1)
            print ("Login successful!")
            logged()

        else:
            print ("Password did not match!")

def logged():
    time.sleep(1)
    print ("Welcome to ----")

main()