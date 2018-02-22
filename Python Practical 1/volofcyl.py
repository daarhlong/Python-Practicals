#getting radius n length
rad = float(input("Input radius(cm): "))
length = float(input("Input length(cm): "))
pi = 3.14
#compute area n vol
area = rad * rad * pi
volume = area * length

print("Volume of cylinder is {0}cm\u00b3".format(volume))
