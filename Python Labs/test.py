import random
import csv

#Student registration

def studentregistration(studentdict={}):
    templist = []
    fn = input("Enter your first name: ")
    sn = input("Enter your surname: ")
    pn = input("Enter your phone number: ")
    ea = input("Enter your email address: ")
    pswd = input("Create a password: ")

    while(True):
        studentid = random.randint(1, 1000)
        if studentid not in studentdict.keys:
                templist.append(fn)
                templist.append(sn)
                templist.append(pn)
                templist.append(ea)
                templist.append(pswd)
                templist.append(100)
                templist.append(studentID)
                templist.append("Module 1 to be selected")
                templist.append("Module 2 to be selected")
                studentdict[studentID]=templist
                print("Mr/Ms ", fn, sn, ", your unique student ID is ", studentid, "")
                break

#Module selection

def moduleselect(moduledict = {}):
    print("You will be asked to select two of the following modules to study:"
          "\n1. Programming 1"
          "\n2. Programming 2"
          "\n3. Networking 1"
          "\n4. Mathematics"
          "\nB. Return to main page")

    for item in moduledict{}:
        module1 = input("Please select your first module:")
        module2 = input("Please select your second module:")

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
    for item in topuplist:
        studentpoints = item[5]
    topup = input("How many points would you like to deposit?")
    conftopup = input("Are you sure you would like to deposit " + topup + " points")
    add = int(topup)

        if conftopup in ['y', 'Y', 'yes', 'Yes', 'YES']:
            studentpoints = (studentpoints + add)
            balance = str(studentpoints)
            print("Your new balance is " + balance)
            item[5] = balance
        else:
            print("Please try again.")





#Shopping

def shopping(shoppinglist = []):
    print("Select an option for shopping:"
          "\n1. Pages"
          "\n2. Food portions"
          "\nB. Return to main page")
    shoppingoption = input("Select an option:")

    for item in shoppinglist:
        if shoppingoption == "1":
            pagequantity = float(input("How many pages would you like to print?"))
            cost = 0.2 * pagequantity
            if cost > item[5]:
                print("Sorry, there are insufficient funds in your account")
                break
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
        elif shoppingoption == "b" or shoppingoption == "B":
            break





#Check balance

def checkbalance(balancelist=[]):

    for item in balancelist:
        print("\nMr/Ms ", item[0], item[1], " Points Balance:", item[5], "")

#Edit information

def editinfo(editlist=[]):
    editoption = input("Select an option to edit information:"
                       "\n1. Email address"
                       "\n2. Phone number "
                       "\n3. Password"
                       "\nB. Return to main menu")

    for item in editlist:
        if editoption == "1":
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
    for item in reportlist:
        print("The following students are registered: ")
        print("\nMr/Ms ", item[0], item[1], " contact number:", item[2], "Email address: ", item[3], "."
                      "\nYou have chosen to study:", item[7], "and", item[8], ".")




stu = list()


print("Welcome to the student registration program.")

while (True):
    print("\nPlease select one of the following options:"
             "\n1. Student registration"
             "\n2. Module selection and verification"
             "\n3. Student account top-up"
             "\n4. Shopping"
             "\n5. Check Balance"
             "\n6. Edit information"
             "\n7. Reporting"
             "\nQ. Quit")
    menuoption = input("Select an option: ")

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

print(stu)