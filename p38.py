"""
55555
4  4
3 3
22
1

"""
n=int(input("Enter a num = "))
for i in range(1, n+1):
    print()
    for j in range(1, n+1):
        if j==1 or i==1 or i+j==n+1:
            print(n-i+1,end="")
        else:
            print(" ",end="")