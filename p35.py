"""
*****
*  *
* *
**
*

"""
n=int(input("enter a num = "))
for i in range(1, n+1):
    print()
    for j in range(1, n+1):
        if j==1 or i==1 or i+j==n+1 :
            print("*",end="")
        else:
            print(" ",end="")
