import csv

customers = open('customers.csv','r')

customer_file = csv.reader(customers, delimiter=',')

outfile = open('customer_country.csv', 'w')

outfile.write('Full Name, Country\n')


next(customer_file)

for record in customer_file:

    first_name = record[1]
    last_name = record[2]
    Country =  record[4]
    full_name = first_name + ' ' + last_name 

    outfile.write(full_name + ',' + Country +'\n')

outfile.close()