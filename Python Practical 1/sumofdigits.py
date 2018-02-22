num = int(input("Enter integer here: "))

#last digit = (num %10)
#second digit = (num // 10) % 10
#third digit = (num // 10) // 10

sumofdigits = (num % 10) + (num // 10) % 10 + (num // 10) // 10


def function():

    if 0 < num < 1000:
        print("The sum of the digits in the integer is", sumofdigits)
       
    else:
        print("You can only enter an integer between 0 and 1000")
        
function()    



