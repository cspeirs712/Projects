import csv

#1 student reg
firstname = input("Enter your first name")
surname = input("Enter your surname:")
phonenum = input("Enter your phone number:")
email = input("Enter your email address:")
password = input("Create a password:")
studentpoints = 100
studentID
print("Your unique student ID is: "+studentID)

#2 module selection
module1
module2
print("Your current modules are: "+ module1+" "+module2+"")

#3 account topup

topup = input("How many points would you like to deposit?")
conftopup = input("Are you sure you would like to deposit " + topup + " points")
add = int(topup)
if conftopup in ['y', 'Y', 'yes', 'Yes', 'YES']:
    studentpoints = (studentpoints+add)
    balance=str(studentpoints)
    print("Your new balance is " + balance)

#5 check balance

print(firstname, surname)
print(studentpoints)

#6 Edit information
editoption = input("To edit information press 1 for email address. Press 2 for phone number. Press 3 for password.")
if editoption in ['1', 'one', 'One', 'ONE']:
    email = input("Please enter your new email address")
elif editoption in ['2', 'two', 'Two', 'TWO']:
    phonenum = input("Please enter your new phone number:")
elif editoption in ['3', 'three', 'Three', 'THREE']:
    password = input("Please enter your new password:")

#7 reporting(add studentID)
print("The following is all information stored about you:")
print(firstname, surname)
print(phonenum)
print(email)

#student login(fully working to be implemented)
credID = int(input("Please enter your student ID:"))
found = 0
for item in reportlist:
    if credID == item[6]:
        credPasswd = input("please enter your password:")
        if credPasswd == item[4]:
            print("Log-in Successful!")
            break
        else:
            print("Log-in Failed!")
            break
    else:
        print("Log-in Failed!")
        break
#put back into program at reporting module
print("The following students are registered: ")
    for item in reportlist:
        print("\nMr/Ms ", item[0], item[1], " contact number:", item[2], "Email address: ", item[3],"."
              "\nYou have chosen to study:", item[7],"and", item[8],".")




credID = int(input("Please enter your student ID:"))

for item in reportlist:
    if credID == item[6]:
        credPasswd = input("please enter your password:")
        if credPasswd == item[4]:
            print("The following students are registered: ")
            print("\nMr/Ms ", item[0], item[1], " contact number:", item[2], "Email address: ", item[3], "."
                  "\nYou have chosen to study:", item[7], "and", item[8], ".")
            break
        else:
            print("Log-in Failed!")
            break
    else:
        print("Log-in Failed!")
        break

