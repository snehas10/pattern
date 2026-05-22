"""
12345
12345
12345
12345
12345

"""
n=int(input("enter a num = "))
for i in range(1, n+1):
    print()
    for j in range(1, n+1):
        if j==i or j<=n:
            print(j,end="")
            