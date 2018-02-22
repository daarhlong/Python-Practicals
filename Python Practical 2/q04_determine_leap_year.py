def func():
    entyr = int(input("Enter year: "))
    while entyr != 0:
        if (entyr % 4) == 0:
            print("Leap")
        elif (entyr % 400) == 0:
            print("Leap")
        else:
            print("Non-Leap")
        return func()

    if entyr == 0:
        print("Error")

func()
