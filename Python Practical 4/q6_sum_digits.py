def sum_digits(n):
    if n%10 < 1:
        return n
    else:
        return (n%10) + sum_digits(n//10)
print(sum_digits(234))
