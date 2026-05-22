"""
12345
1234
123
12
1

"""
n=int(input("Enter a num = "))
for i in range(1, n+1):
    print()
    for j in range(1, n-i+2):
        print(j,end="")
