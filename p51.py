"""
12345
 1__4
  1_3
   12
    1

"""
n=int(input("Enter num ="))
for i in range(n, 0, -1):
    print()
    for j in range(n-i):
         print(" ",end="")
    for k in range(1, i+1):
        if k==1 or i==n or k==i:
            print(k,end="")
        else:
            print("_",end="")
