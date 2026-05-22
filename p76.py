'''
x
xx
xxx
xxxx
xxx
xx
x

'''

n=int(input("enter number"))
for i in range(1,n):
    print()
    for j in range(1,i+1):
         print("*",end="")
for i in range(n-2,0,-1):
    print()
    for j in range(1,i+1):
         print("*",end="")