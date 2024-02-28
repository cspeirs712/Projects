#imports csv file type
import csv
#define the dictionary
dict = {1 : 'Hello', 2 : 'Hi',3 : 'bye'}
#create and open the file to store the dictionary
file = open('dictionary.csv', 'w+', newline='')
#write the drictionary into the file
with file:
    write = csv.writer(file)
    write.writerow(dict)
#open the dictionary.csv file and read the contents into the program
with open('dictionary.csv', newline = '') as f:
    reader = csv.reader(f)
    newDict = list(reader)
#print the contents onto the program
print(newDict)