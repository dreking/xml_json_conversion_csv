import json
import csv

#import json data into python file
f = open('transactions.json')   
transactions_data = json.load(f)
f.close()

# open a file for writing
trans_data = open('transactions.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(trans_data)

count = 0
trans_values = []
for emp in transactions_data:
      if count == 0:
             header = emp.keys()
             csvwriter.writerow(header)
             count += 1
      csvwriter.writerow(emp.values())
trans_data.close()
