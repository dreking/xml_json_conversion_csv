import xml.etree.ElementTree as ET
import json
import csv

#import xml data 
tree = ET.parse("customers.xml")
root = tree.getroot()

#import json data 
f = open('transactions.json')   
transactions_data = json.load(f)
f.close()

# open a file for writing
trans_data = open('transactions.csv', 'w')
csvwriter = csv.writer(trans_data)

#retrieving customer info from xml file
cus_info = []
for member in root.findall('customer'):
        cus_info.append(member.find('id').text)
        cus_info.append(member.find('name').text)

#Generating City Text from Google Maps
cityNames = ["16 KK 16 Ave, Kigali, Rwanda", 'KU Plaza, Nairobi, Kenya', 'Johannesburg CBD Bus Stop, Von Wielligh St, Johannesburg, 2000, South Africa']

#adding name of customer to the transaction data
count = len(transactions_data)
for i in range(count):
        if transactions_data[i]['customerId'] == 1:
                transactions_data[i].update({"customerName":cus_info[1]})
                transactions_data[i].pop('latitude')
                transactions_data[i].pop('longitude')
                transactions_data[i].update({"CityName":cityNames[0]})
                transactions_data[i].update({"TransactionId":i+1})
        elif transactions_data[i]['customerId'] == 2:
                transactions_data[i].update({"customerName":cus_info[3]})
                transactions_data[i].pop('latitude')
                transactions_data[i].pop('longitude')
                transactions_data[i].update({"CityName":cityNames[1]})
                transactions_data[i].update({"TransactionId":i+1})
                
        elif transactions_data[i]['customerId'] == 3:
                transactions_data[i].update({"customerName":cus_info[5]})
                transactions_data[i].pop('latitude')
                transactions_data[i].pop('longitude')
                transactions_data[i].update({"CityName":cityNames[2]})
                transactions_data[i].update({"TransactionId":i+1})
                
#writing all transactions to file
a = 0
for emp in transactions_data:
      if a == 0:
             header = emp.keys()
             csvwriter.writerow(header)
             a += 1
      csvwriter.writerow(emp.values())

print("Writing to transactions.csv file done!")
trans_data.close()


