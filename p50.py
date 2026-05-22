"""
55555
 4444
  333
   22
    1

"""
n=int(input("Enter num ="))
for i in range(n, 0, -1):
    print()
    for j in range(n-i):
         print(" ",end="")
    for k in range(1, i+1):
         print(i,end="")