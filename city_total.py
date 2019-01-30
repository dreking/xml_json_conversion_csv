import json
import csv

#import json data 
f = open('transactions.json')   
transactions_data = json.load(f)
f.close()

# open a file for writing
trans_data = open('city_totals.csv', 'w')
csvwriter = csv.writer(trans_data)

#Generating City Names fro Google Maps
cityNames = ['16 KK 16 Ave, Kigali, Rwanda', 'KU Plaza, Nairobi, Kenya', 'Johannesburg CBD Bus Stop, Von Wielligh St, Johannesburg, 2000, South Africa']

#Generating totals for all customers
count = len(transactions_data)
t1 = {}
t2 = {}
t3 = {}
city_totals = []
#Generating details for First customer
count_trans = 0
amount = 0
for i in range(count):
    if transactions_data[i]['customerId'] == 1:
        amount += transactions_data[i]['amount']
        count_trans += 1
        t1.update({"cityName" : cityNames[0]})
        t1.update({"amount": amount})
        t1.update({"Unique_customer" : 1})
        t1.update({"Total_Transactions" : count_trans})
city_totals.append(t1)

#Generating details for Second Customer
count_trans = 0
amount = 0
for i in range(count): 
    if transactions_data[i]['customerId'] == 2:
        amount += transactions_data[i]['amount']
        count_trans += 1
        t2.update({"cityName" : cityNames[1]})
        t2.update({"amount": amount})
        t2.update({"Unique_customer" : 2})
        t2.update({"Total_Transactions" : count_trans})
city_totals.append(t2)

#Generating details for Third Customer
count_trans = 0
amount = 0
for i in range(count):
    if transactions_data[i]['customerId'] == 3:
        amount += transactions_data[i]['amount']
        count_trans += 1
        t3.update({"cityName" : cityNames[2]})
        t3.update({"amount": amount})
        t3.update({"Unique_customer" : 3})
        t3.update({"Total_Transactions" : count_trans})
city_totals.append(t3)

#writing all totals to csv
a = 0
for emp in city_totals:
      if a == 0:
             header = emp.keys()
             csvwriter.writerow(header)
             a += 1
      csvwriter.writerow(emp.values())

print("Writing to city_totals.csv file done!")
trans_data.close()


