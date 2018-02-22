def func():
    year = int(input("Enter year: "))
    month = int(input("Enter month as integer: "))
    while 1 <= month <= 12:
        if ((year % 4) == 0 or (year % 400) == 0) and month == 2:
            print("Days: 29")
        elif month == 2:
            print("Days: 28")
        elif (month % 2) == 0:
            print("Days: 30")
        elif (month % 2) != 0:
            print("Days: 31")
        else:
            print("Please enter valid month")
        return func()
func()
