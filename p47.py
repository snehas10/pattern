"""
    A
   AB
  A_C
 A__D
ABCDE

"""
n=int(input("enter a num= "))
for i in range(1, n+1):
    print()
    for j in range(1, n-i+1):
        print(" ",end="")
    ch=65    
    for k in range(1, i+1):
        if k==1 or k==i or i==n:
            print(chr(ch),end="")
        else:
            print("_",end="")
        ch+=1    
