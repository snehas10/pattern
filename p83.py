'''
\     /
 \   /
  \ /
   *
  / \
 /   \
/     \

'''

n=int(input("enter the number :"))

for i in range(1,n+1):
    print()
    
    for j in range(2,i+1):
        print(" ",end="")
    if i==n:
       print("O",end="")
    else:
       print("\\",end="")

    for k in range(n-i,0,-1):
        print(" ",end="")
    for k in range(n-i,1,-1):
        print(" ",end="")
    if i<=n-1:
       print("/",end="")


for i in range(n-1,0,-1):
    print()
    
    for j in range(2,i+1):
        print(" ",end="")
    print("/",end="")

    for k in range(n-i,0,-1):
        print(" ",end="")
    for k in range(n-i,1,-1):
        print(" ",end="")
    print("\\",end="")
