def gcd(m, n):
    if m < n:
        d = m
    elif n < m:
        d = n
    while n % d !=0 or m % d != 0:
        d = d-1
    print("{0} is the greatest common divisor.".format(d))

gcd(24, 16)
gcd(255, 25)
