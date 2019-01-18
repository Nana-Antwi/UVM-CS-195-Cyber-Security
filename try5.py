#Music legend program
#Nana Antwi


#define the function


#user prompt
user_prompt = input('Do you wish to create a music legend database account: ', 'yes/no')

#condition loop statments
if user_prompt == 'yes':
     print('Welcome to Music Legend')
     print('Follow the steps to create your account')
     print('Fill out with correct information')


#open the file to write information to
myfile = open('musiclegend.txt', 'w')

#account creation
username = input('Enter the name you wish to use as username for your account:')
password = input('Enter the password you wish to use as password for your account:')
print('Thank you for creating and account with music legend')

#log in
print('Enter your log-in inforamation')
log_name = input('Enter your username:')
log_password = input('Enter your password')


#log in condition loop statements
log_name == username
log_password == password

#validation
if log_name == username:
     
else:
     print('Entry error enter your username again:')
    log_name = input('Enter your username:')

if log_password == password:
     
else:
     print('Entry error enter your password again: ')
     log_password = input('Enter your password')


#collection varaiables
report_time = input("Enter your time report: ")
days_off = input("Resquest a day off: ")
accounting = input("Enter accounting report: ")
forum = input("Post on community forum: ")
training  = input("Enter training completed: ")
help_desk = input("Enter questions for help desk: ")


#write to file
myfile.write(name)
myfile.write(artist)
myfile.write(genre)
myfile.write(albums)
myfile.write(song)
myfile.write(quality)

#read information from file and display it 
index = 0
for line in myfile:
index += 1
line = line.rstrip("\n")
print(line)


#display results 
print('The name of your favorite artist:', line, index +1)
print('The genere of music he performs', line, index += 1)
print('The number of albums to his credit', line, index +=1)
print('Your favorite song all time by him', line, index +=1)
print('The quality you attribute to his work', line, index +=1)

#if no on userprompt
if user_prompt == 'no'
print('Music Legend program is closed')


#close input file 
myfile.close()















