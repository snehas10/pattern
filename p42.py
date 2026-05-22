"""
54321
5432
543
54
5

"""
n=int(input("Enter a num = "))
for i in range(1, n+1):
    print()
    for j in range(1, n+1):
        if j<=n-i+1:
            print(n-j+1,end="")