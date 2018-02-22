def func():
    numb = int(input("Enter number:"))
    while numb != 0:
        detint = numb % 2
        if detint == 0:
            print("{0} is even".format(numb))
        elif detint != 0:
            print("{0} is odd".format(numb))
        else:
            print("Error")
        return func()
    
    if numb == 0:
        print("Error")
func()

