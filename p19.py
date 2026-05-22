"""
*
* *
*   *
*     *
* * * * *

"""
n=int(input("Enter a num = "))
for i in range(1, n+1):
    print()
    for j in range(1, n+1):
        if j==1 or j==i or i==n:
            print("*",end="")
        else:
            print(" ",end="")
            