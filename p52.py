"""
55555
 4__4
  3_3
   22 
    1

"""
n=int(input("Enter num ="))
for i in range(n, 0, -1):
    print()
    for j in range(n-i):
         print(" ",end="")
    for k in range(1, i+1):
         if k==1 or k==i or i==n:
            print(i,end="")
         else:
             print("_",end="")
             