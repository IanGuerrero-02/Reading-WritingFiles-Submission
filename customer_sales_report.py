import csv

sales = open('sales.csv', 'r')

sales_report = csv.reader(sales)

outfile = open('salesreport.csv', 'w')

outfile.write('CustomerID Total\n')

next(sales_report)

totals = {}

for rec in sales_report:
    id = rec[0]
    subtotal = float(rec[3])
    tax = float(rec [4])
    freight = float(rec [5])
    total = subtotal + tax + freight 
    if id in totals:
        totals[id] += total
    else: 
        totals[id] = total


for id in totals:
    outfile.write(f"{id} {totals[id]:.2f}\n")

outfile.close()