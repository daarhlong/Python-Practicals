n = int(input("Enter integer: "))
def display_pattern(n):
    s = ' '
    p = 1
    for r in range(1, n+1):
        for i in range(1, n+1):
            print(s ,end=' ')
        print(p)
    s = s-1
    p = p+1
    
    
    
display_pattern(n)
        
    
    
