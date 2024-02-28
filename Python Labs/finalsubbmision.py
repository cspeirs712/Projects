#Craig Speirs
#
#imporing the relevant modules for use within the program
import random
import csv

#Student registration

#Define the module for the student registration code
def studentregistration(studentlist=[]):
    #create a temporary list
    templist = []
    #recieve all information from users
    fn = input("Enter your first name: ")
    sn = input("Enter your surname: ")
    pn = input("Enter your phone number: ")
    ea = input("Enter your email address: ")
    pswd = input("Create a password: ")

    #creating while loop to check if student ID has been used before
    while(True):
        #using random number function to assign a number between 1 and 1000 as student id
        studentid = random.randint(1, 1000)
        if studentid not in studentlist:
            #apppending all information into a temporary list
                templist.append(fn)
                templist.append(sn)
                templist.append(pn)
                templist.append(ea)
                templist.append(pswd)
                templist.append(100)
                templist.append(studentid)
                templist.append("Module 1 to be selected")
                templist.append("Module 2 to be selected")
                #appending the temp list into the student list as 1 item consisting
                #of the items in the temp list
                studentlist.append(templist)
                #Printing the students id after it has been assigned
                print("Mr/Ms ", fn, sn, ", your unique student ID is ", studentid, "")
                break

#Module selection

def moduleselect(modulelist = []):
    #Creating a menu for the module selection
    print("You will be asked to select two of the following modules to study:"
          "\n1. Programming 1"
          "\n2. Programming 2"
          "\n3. Networking 1"
          "\n4. Mathematics"
          "\nB. Return to main page")

    #for loop to take inputs and using if statements to assign values
    for item in modulelist:
        module1 = input("Please select your first module:")
        module2 = input("Please select your second module:")
        #if statements to assign values to items in the list for modules, the statement takes the input entered by the
        #users to make the decision of what to set the module to. If the input by the user doesnt match any of the
        #options it tajes the program back to the main page
        if module1 in ["b", "B"] or module2 in ["b", "B"]:
            break
        if module1 == "1":
            print("You have chose to study Programming 1!")
            choice = "Programming 1"
            item[7] = choice
        elif module1 == "2":
            print("You have chose to study Programming 2!")
            choice = "Programming 2"
            item[7] = choice
        elif module1 == "3":
            print("You have chose to study Networking 1!")
            choice = "Networking 1"
            item[7] = choice
        elif module1 == "4":
            print("You have chose to study Mathematics!")
            choice = "Mathematics"
            item[7] = choice

        if module2 == module1:
            print("Please select two different modules")
            break
        elif module2 == "1":
            print("You have chose to study Programming 1!")
            choice = "Programming 1"
            item[8] = choice
        elif module2 == "2":
            print("You have chose to study Programming 2!")
            choice = "Programming 2"
            item[8] = choice
        elif module2 == "3":
            print("You have chose to study Networking 1!")
            choice = "Networking 1"
            item[8] = choice
        elif module2 == "4":
            print("You have chose to study Mathematics!")
            choice = "Mathematics"
            item[8] = choice



#Student account

def accounttopup(topuplist=[]):
    #for lopp used to assign student points as the corresponding item in the loop
    for item in topuplist:
        studentpoints = item[5]
    topup = input("How many points would you like to deposit?")
    conftopup = input("Are you sure you would like to deposit " + topup + " points")
    #could be removed and set the input for the topup variable straight to integer for efficiency
    add = int(topup)
    #if statement used to validate the input, if input doesnt match print message and returns program
    #to main page
    if conftopup in ['y', 'Y', 'yes', 'Yes', 'YES']:
        #adds the topup amount entered to current number of points in the account
        studentpoints = (studentpoints + add)
        #sets the balance to string to be used within a print statement to print the new balance
        balance = str(studentpoints)
        print("Your new balance is " + balance)
        item[5] = balance
    else:
        print("Please try again.")





#Shopping

def shopping(shoppinglist = []):
    #printing shopping menu  and taking user input
    print("Select an option for shopping:"
          "\n1. Pages"
          "\n2. Food portions"
          "\nB. Return to main page")
    shoppingoption = input("Select an option:")

    #for loop to state items used to work are in the shoppinglist
    for item in shoppinglist:
        #if statements to take input and do process to create output
        if shoppingoption == "1":
            #input taken then multiplied with the cost to create a final cost and print a reciept
            pagequantity = float(input("How many pages would you like to print?"))
            cost = 0.2 * pagequantity
            #if statement used to ensure that the balance within student account cannot end as negative after shopping
            if cost > item[5]:
                print("Sorry, there are insufficient funds in your account")
                break
            #taking the new account balance and assigning it to relevant item within list
            accountbalance = item[5] - cost
            item[5] = accountbalance
            print("The cost of your shopping is", cost, "point(s) and your account balance is",
                  accountbalance, "point(s).")
        elif shoppingoption == "2":
            foodquantity = float(input("How many food portions would yoy like to order?"))
            cost = 2 * foodquantity
            if cost > item[5]:
                print("Sorry, there are insufficient funds in your account")
                break
            accountbalance = item[5] - cost
            item[5] = accountbalance
            print("The cost of your shopping is", cost, "point(s) and your account balance is",
                  accountbalance, "point(s).")
        #statement used to return to main menu if user inputs b
        elif shoppingoption == "b" or shoppingoption == "B":
            break





#Check balance

def checkbalance(balancelist=[]):
    #takes the studentpoints item from the balance lists and displays it alongside students name
    for item in balancelist:
        print("\nMr/Ms ", item[0], item[1], " Points Balance:", item[5], "")

#Edit information

def editinfo(editlist=[]):
    #menu for editing information and input for the option of the user
    editoption = input("Select an option to edit information:"
                       "\n1. Email address"
                       "\n2. Phone number "
                       "\n3. Password"
                       "\nB. Return to main menu")

    for item in editlist:
        #if statements used to check input and do a process to create an output if the input and option matches
        if editoption == "1":
           #takes the input and assigns the new information to the relevant item in the list
            newemail = input("Please enter your new email address.")
            item[3] = newemail
        elif editoption == "2":
            newphone = input("Please enter your new phone number.")
            item[2] = newphone
        elif editoption == "3":
            newpass = input("Please enter your new password.")
            item[4] = newpass
        elif editoption == "b" or editoption == "B":
            break






#Reporting

def reporting(reportlist = []):
    print("The following students are registered: ")
    for item in reportlist:
        #prints the information for the students onto the screen using some formatting to ensure all messages appear the same

        print("\nMr/Ms ", item[0], item[1], " contact number:", item[2], "Email address: ", item[3], "."
                      "\nYou have chosen to study:", item[7], "and", item[8], ".")

#Main Program
#creates the list used to define all modules
stu = list()

with open("studentstorage.csv", "r") as r:
    reader = csv.reader(r)
    stu = list(reader)
#welcome message for the program
print("Welcome to the student registration program.")
#while used to create an infinite loop to keep the menu reappearing everytime a process is finished
while (True):
    #Print the mian menu with detailed options for the user
    print("\nPlease select one of the following options:"
             "\n1. Student registration"
             "\n2. Module selection and verification"
             "\n3. Student account top-up"
             "\n4. Shopping"
             "\n5. Check Balance"
             "\n6. Edit information"
             "\n7. Reporting"
             "\nQ. Quit")
    #takes the input from the user
    menuoption = input("Select an option: ")

    #if statement covering all plausible inputs from the user, when the program finds the match to the input
    #it calls the modules defined above, if the input is Q then the program will end
    #creating the menu structure like this ensures when a process end the menu will always reappear for the user.
    if menuoption == "Q" or menuoption == "q":
        break
    elif menuoption == "1":
        studentregistration(stu)
    elif menuoption == "2":
        moduleselect(stu)
    elif menuoption == "3":
        accounttopup(stu)
    elif menuoption == "4":
        shopping(stu)
    elif menuoption == "5":
        checkbalance(stu)
    elif menuoption == "6":
        editinfo(stu)
    elif menuoption == "7":
        reporting(stu)

with open("studentstorage.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(stu)

#this is the code for verifying the student within the program, i had implemented this into the modules but came across
#multiple errors during testing the finished program. I spent a period of time trying to troubleshoot these errors but
#couldnt find a soloution that worked for all of the modules so i decided to remove the code in order to create no errors
#after submission

#credID = int(input("Please enter your student ID:"))

#for item in reportlist:
    #if credID == item[6]:
        #credPasswd = input("please enter your password:")
        #if credPasswd == item[4]:
            #print("The following students are registered: ")
            #print("\nMr/Ms ", item[0], item[1], " contact number:", item[2], "Email address: ", item[3], "."
                  #"\nYou have chosen to study:", item[7], "and", item[8], ".")
            #break
        #else:
            #print("Log-in Failed!")
            #break
    #else:
        #print("Log-in Failed!")
        #break
