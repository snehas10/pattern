"""
11111
 2222
  333
   44
    5

"""
n=int(input("Enter num ="))
l=1
for i in range(n, 0, -1):
    print()
    for j in range(n-i):
         print(" ",end="")
    for k in range(1, i+1):
         print(l,end="")
    l=l+1