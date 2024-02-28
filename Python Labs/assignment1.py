# declare the list used to store data
Information =  []

# use of while loop to continue to receive data input until loop is broken
while True:
# receive input from users
 first = input("Please enter your first name:")
 last = input("Please enter your last name:")
 studentID = input("Please enter your student ID:")
# add information into the list
 Information.append([first, last, studentID])
# looking for the condition used to break the loop
 if first == "0":
    break
 elif last == "0":
    break
 elif studentID == "0":
    break

# pop function used to remove last index from list. This is done so that when search occurs later
# in program there isnt an index with student id 0 as 0 is used to end program
Information.pop()

# notify the user search mode is now in operation
print("You are now entering search mode!")

# initialise result variable
result  = False

# while loop used to check condition
while result == False:
# receive input from the user for ID to search
 SearchID = input("Enter a student ID to search records:")
# for loop used for search and display of results
 for studentID in Information:
         if SearchID in studentID:
             print(studentID)
             # setting result variable to true
         result = True
# if statement to verify condition to end progran
 if SearchID == "0":
     # tells user program has been ended sucessfully
     print("Program now ending")
     # breaks loop and ends program
     break
# resets loop to continue searching if program hasnt ended
 else:
     result = False