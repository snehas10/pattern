"""
ABCDE
 ABCD
  ABC
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
         print(chr(ch),end="")
         ch+=1