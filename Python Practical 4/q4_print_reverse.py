def reverse(n):
    if n%10 < 1:
        return n
    else:
        print(n % 10, end='')
        reverse(n//10) 
    
reverse(123345)
