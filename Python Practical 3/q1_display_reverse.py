n = int(input("Enter integer: "))

def reverse_int(n):
    strang = len(str(n))
    if strang == 1:
        print(n)
    elif strang != 1:
        for i in range(strang):
            print(n % 10, end='')
            n = n // 10
        
reverse_int(n)
        
        
        
    
