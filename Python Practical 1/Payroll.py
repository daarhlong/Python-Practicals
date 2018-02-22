name = input("Enter name: ")
hours = int(input("Enter number of hours worked weekly: "))
pay = float(input("Enter hourly pay rate($): "))
cpf = float(input("Enter CPF contribution rate(%): "))

grosspay = hours * pay
cpfcontri = float((cpf / 100) * grosspay)
netpay = grosspay - cpfcontri

print('')
print("Payroll statement for", name)
print("Number of hours worked in week: ", hours)
print("Hourly pay rate: ", pay)
print("Gross pay =",grosspay)
print("CPF contribution at {0}% = {1:.2f} ".format(cpf,cpfcontri))
print('')
print("Net pay = ${0:.2f}".format(netpay))
