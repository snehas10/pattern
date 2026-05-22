'''
    1
    2
    3
    4
123454321
    4
    3
    2
    1
'''

n=int(input("enter the number "))
for i in range(1,n):
    print()
    for j in range(1,n):
         print(" ",end="")
    print(i,end="")
print()
for j in range(1,n+1):
    print(j,end="")
for j in range(n-1,0,-1):
    print(j,end="")
for i in range(n-1,0,-1):
    print()
    for j in range(1,n):
         print(" ",end="")
    print(i,end="")