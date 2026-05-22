"""
5
54
543
5432
54321

"""
n=int(input("Enter a num = "))
for i in range(1, n+1):
    print()
    for j in range(n, n-i, -1):
           print(j ,end="")