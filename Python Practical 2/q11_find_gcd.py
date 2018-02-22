n1 = int(input("Enter integer 1: "))
n2 = int(input("Enter integer 2: "))
if n1 < n2:
    d = n1
elif n2 < n1:
    d = n2
while n1 % d != 0 or n2 % d != 0:
    d = d-1
print("{0} is the greatest common divisor.".format(d))

    
