print("Miles\t\tKilometers\tKilometres\tMiles")
for x in range(1,11):
    print("{0}\t\t{1:.3f}\t\t{2}\t\t{3:.3f}".format(x, x*1.609, x*5+15, (x*5+15)/12.43))
