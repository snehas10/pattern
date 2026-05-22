"""
    *
   ***
  *****
 *******
*********
    

"""
n=int(input("Enter a num ="))
for i in range(1, n+1):
    print()
    for j in range(0, n-i):
        print(" ",end="")
    for k in range(1, i+1):
        print("*",end="")
    for l in range(i-1,0,-1):
        print("*",end="")
        