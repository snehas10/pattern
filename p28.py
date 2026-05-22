"""
1
123
12345
1234567
123456789

"""
n=int(input("Enter a num = "))
for i in range(1,n+1):
    print()
    for j in range(1, 2*i):
        print(j,end="")
        