num = int(input("Enter Integer: "))
A = []
while num % 2 == 0:
    A.append(2)
    num = num / 2
while num % 3 == 0:
    A.append(3)
    num = num / 3
for i in range(5, int(num)+1, 2):
    while num % i == 0:
        A.append(i)
        num = num / i
print(A)
