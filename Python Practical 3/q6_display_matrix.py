import random
n = int(input("Enter integer for matrix: "))
def print_matrix(n):
    counter = 1
    for i in range(n):
        while counter <= n:
            print(random.randint(0,1),end=' ')
            counter += 1
        if counter > n:
            print("\n")
            counter = 1

print_matrix(n)
