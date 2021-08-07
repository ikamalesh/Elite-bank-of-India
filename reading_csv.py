import csv



number = input('Enter number to find\n')
csv_file = csv.reader(open('india.csv', "r"), delimiter=",")


#loop through the csv list
for row in csv_file:
    if number == row[0]:
         for item in row:
             print(item.title())