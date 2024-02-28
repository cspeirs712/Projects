#import csv extension
import csv

#declare the list to be read/written
ls = ['hello', 'hi', 'bye']

#create and open the list.csv file then use the csv writer to read the list and write it into the file
file = open('list.csv', 'w+', newline='')
with file:
    write = csv.writer(file)
    write.writerow(ls)

#open the list.csv file  the use the reader to read the contents of the file and write into a python list
with open('list.csv', newline = '') as f:
    reader = csv.reader(f)
    newlist = list(reader)

#print the new list
print(newlist)