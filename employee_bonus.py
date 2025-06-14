import csv

employee = open('employee_data.csv','r')

employee_file = csv.reader(employee)

outfile = open('employeePay.csv' , 'w')

next(employee_file)

for rec in employee_file:
    Name = rec[1]
    Salary = rec[3]
    Bonus = rec[7]
    pay = Salary + Bonus

    outfile.write(f'Name: {Name}\n')
    outfile.write(f'Salary: ${Salary}\n')
    outfile.write(f'Bonus: ${Bonus}\n')
    outfile.write(f'Pay: ${pay}\n')
   



outfile.close()
