i = int(input("Enter integer: "))
def m_series(i):
    A = []
    m = 1
    n = 2
    for r in range(1, i+1):
        p = m / n
        A.append(p)
        m = n
        n = n + 1
        x = sum(A)
        print("{0}\t\t{1:.4f}".format(r, x))
    
print("i\t\tm(i)")
m_series(i)
