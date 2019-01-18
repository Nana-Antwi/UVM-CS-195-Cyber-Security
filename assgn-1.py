#Nana Antwi 
#Assignment 1 
#Username Password Database Program
#Humanresourceware.py

#Design a program that prompt users to create account with a username and password to access a companys human resource services.

#import python library
import os 

#define main function
def main():

        


        #output statements 
        print("Humanresource-Ware Program!")

        #user prompt input statements 
        user_prompt = input("Do you wish to create a humanresoure-ware account yes/no: ")

        #condition loop statments
        if user_prompt == "yes":
                print("Welcome to Humanresource-Ware!!!")
                print("Follow the steps to create your account.")
                print("Fill out with the correct information.")


                #account creation
                username = input("Enter the name you wish to use as username for your account:")
                print("Your username for this account is:", username)
                print("Thank you for creating an account.")


                #open the file to write information to
                myfile = open(username+".txt", "a")

                #Input prompt
                input_prompt = input("Do you wish to add information to your humanresoure-ware account yes/no: ")

                #condtion loop state aoff adding new  information.
                if input_prompt == "yes":
                    print("Add information to your account")



                    #data base question to ask.
                    report_time = input("Enter your time report: ")
                    days_off = input("Request days off: ")
                    accounting = input("Enter accounting report:")
                    forum = input("Post in community forum:")
                    help_desk = input("Enter questions for the help desk:")


                    #write database information to a file
                    myfile.write("Time Report:"+report_time+"\n")
                    myfile.write("Days Off:"+days_off+"\n")
                    myfile.write("Accounting Report:"+accounting+"\n")
                    myfile.write("Forum Post:"+forum+"\n")
                    myfile.write("Help Request:"+help_desk+"\n")

                    #Display all user information in account
                    print("You have successfully logged out of your account")
                    print("Your data saved to your account is:")

                    #display save information
                    print("Your information saved:")
                    print("Time Report:", report_time)
                    print("Days Off:", days_off)
                    print("Accounting Report:", accounting)
                    print("Forum Post", forum)
                    print("Help Request", help_desk)
                    print("The above is all the data save on your humanresoure-ware account.")

                    #option of logging back or just quiting to save 
                    log_prompt = input("Do you wish to log back into your humanresource-ware account yes/no: ")


                    #codition loop 
                    if log_prompt == "yes":
                        print("You have logged back into your account!")

                        #if yes 
                        add_prompt = input("Do you wish to to enter new information yes/no: ")
                        if add_prompt == "yes":


                            print("Add new information!")

                            #add new information to work
                            report_time2 = input("Enter your time report: ")
                            days_off2 = input("Request days off: ")
                            accounting2 = input("Enter accounting report:")
                            forum2 = input("Post in community forum:")
                            help_desk2 = input("Enter questions fot the help desk:")


                            #write to file
                            myfile.write("Time Report 2:"+report_time2+"\n")
                            myfile.write("Days off 2:"+days_off2+"\n")
                            myfile.write("Accounting Report 2:"+accounting2+"\n")
                            myfile.write("Forum Post 2:"+forum2+"\n")
                            myfile.write("Help Request 2"+help_desk2+"\n")

                            #display new information
                            print("New information has been successfully added:")
                            print("The new added information:")

                            #display new saved information
                            print("Your information saved:")
                            print("Time Report 2:", report_time2)
                            print("Days Off 2:", days_off2)
                            print("Accounting Report 2:", accounting2)
                            print("Forum Post 2:", forum2)
                            print("Help Request 2:", help_desk2)
                            print("The above is  data save on your humanresoure-ware account.")


                            #all information on your account
                            print("All the data information saved on your humanresoure-ware are:")

                            #userdatabase
                            print("Your total information saved:")
                            print("first entry:")
                            print("Time Report:", report_time)
                            print("Days Off", days_off)
                            print("Accounting Report:", accounting)
                            print("Forum Post:", forum)
                            print("Help Request:", help_desk)
                            print('Second entry:')
                            print("Time Report 2:", report_time2)
                            print("Days Off 2", days_off2)
                            print("Accounting Report 2:", accounting2)
                            print("Forum Post 2:", forum2)
                            print("Help Request 2:", help_desk2)
                            print('The above is all information assocaited with your account')
                            print('Log back in to allow database to process')


                            #close file
                            myfile.close()

                        #valdiation for second enrty
                        elif add_prompt == "no":
                            print("Thanks for using humanresoure-ware")
                            print("Humanresource-Ware has ended!")

                    #validation of codition
                    elif log_prompt == "no":
                        print("You have successfully logged out!")
                        print("Humanresource-Ware has ended")

                        print("Log back in to allow database processing")

                    #prompt again to re-enter user name
                    logname = input("Enter your username with (.txt): ")
            

                    #open save text
                    account_file = open(logname, "r")

                    #read and output contents to program
                    for line in account_file:
                            print(line)

                    #close file
                    account_file.close()

                     #open file
                    user_file = open(logname, "r")

                    #search for an entry
                    search = input("Do you wish to search for information in the database yes/no: ")

                    #condition loop
                    if search == "yes":
                        print("Database Search")
                        print("To search for information in entry one the input format should be: (report_time).")
                        print("To search for information in entry two the input format should be: (report_time2).")


                        #user prompt input.
                        search_entry = input("Enter the entry you wish to search for example (report_time) or (report_time2): ")

                         #convert file into dictionary
                        search_dict = {}
                        for line in user_file:
                                spiltline = line.split(':')
                                search_dict[spiltline[0]] = spiltline[1]
                        print(search_dict[search_entry])
                        #close open input file
                        user_file.close()
                    #validation of codition loop
                    elif search == "no":
                        print("No database search")
                        print("Goodbye!")

                      
                

                    #delete entry
                    delete = input("Do you wish to delete your database yes/no: ")

                    #conditon loop statement 
                    if delete == "yes":
                        os.remove(logname)
                        print("Your humanresoure-ware account has being deleted.")
                        print("Thanks for being a valued user of humanresoure-ware!")

                    elif delete == "no":
                        print("Your database was not deleted.")
                        print("Your are still an authorized user of Humanresource-Ware.")

                            #final display
                        print("Humanresource-ware has finsehed all excutions")

        #if no on userprompt
        elif user_prompt == "no":
            print("Humanresource-Ware is closed")
main()











