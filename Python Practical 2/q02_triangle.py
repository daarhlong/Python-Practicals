side1 = int(input("Enter side 1: "))
side2 = int(input("Enter side 2: "))
side3 = int(input("Enter side 3: "))

if (side1 + side2) > side3 and (side2 + side3) > side1 and (side1 + side3) > side2:
    print(side1 + side2 + side3)
else:
    print("Invalid triangle!")
