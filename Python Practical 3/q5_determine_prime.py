prime = True
def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return prime
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return prime

count = 1
x = 1
for i in range(100):
    while count <= 10:
        if is_prime(x) == True:
            print(x, end=' ')
            count += 1
            x += 1
                
        else:
            x += 1
    else:
        if count > 10:
            print("\n")
        count = 1
        


            
            
            
            



    





