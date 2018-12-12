import xml.etree.ElementTree as ET
import csv

tree = ET.parse("customers.xml")
root = tree.getroot()
# open a file for writing
customer_data = open('customers.csv', 'w')
# create the csv writer object
csvwriter = csv.writer(customer_data)
customer_head = []

count = 0
for member in root.findall('customer'):
	customer = []
	address_list = []
	if count == 0:
		cus_id = member.find('id').tag
		customer_head.append(cus_id)
		cus_name = member.find('name').tag
		customer_head.append(cus_name)
		csvwriter.writerow(customer_head)
		count = count + 1

	cus_id = member.find('id').text
	customer.append(cus_id)
	cus_name = member.find('name').text
	customer.append(cus_name)
	csvwriter.writerow(customer)
Resident_data.close()
