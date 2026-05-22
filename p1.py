"""
*****




"""
n=int(input("Enter nnumber = "))
for i in range(1, 2):
    print()
    for j in range(1, n+1):
        if i==1 and i<=j:
            print("*", end="")
        elif i!=1:
            print(" ",end="")

