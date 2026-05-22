"""
*
 *
  *
   *
    *
"""
n=int(input("Enter a num = "))
for i in range(1,n+1):
    print()
    for j in range(1,n+1):
        if j==i and j<=n:
            print("*",end="")
        else:
            print(" ",end="")
            
