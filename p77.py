'''
1
12
123
1234
123
12
1
'''
n=int(input("enter number"))
for i in range(1,n):
    print()
    for j in range(1,i+1):
         print(j,end="")
for i in range(n-2,0,-1):
    print()
    for j in range(1,i+1):
         print(j,end="")