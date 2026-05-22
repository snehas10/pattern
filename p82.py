'''
   *
  *_* 
 *___* 
*_____*
 *___* 
  *_*
   *
'''

n=int(input("enter the num"))

for i in range(1,n+1):
    print()
    for k in range(1,n-i+1):
        print(" ",end="")
    
    for j in range(1,i*2):
        if j==i*2-1:
            print("*",end="")
        elif j==1:
            print("*",end="")
        else:
            print("_",end="")


for i in range(n-1,0,-1):
    print()
    for k in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,i*2):
        if j==i*2-1:
            print("*",end="")
        elif j==1:
            print("*",end="")
        else:
            print("_",end="")