"""
ABCDE
 A__D
  A_C
   AB
    A

"""
n=int(input("Enter num ="))
for i in range(n, 0, -1):
    print()
    for j in range(n-i):
         print(" ",end="")
    ch=65     
    for k in range(1, i+1):

        if k==1 or i==n or k==i:
            print(chr(ch),end="")
        else:
            print("_",end="")
        ch+=1    