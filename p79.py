'''
1
1 2
1  3
1   4
1  3
1 2
1
'''

n=int(input("enter number"))
for i in range(1,n):
    print()
    for j in range(1,i+1):
         if i==j:
             print(j,end="")
         elif j==1:
             print(j,end="")
         else:
             print(" ",end="")
for i in range(n-2,0,-1):
    print()
    for j in range(1,i+1):
         if i==j:
             print(j,end="")
         elif j==1:
             print(j,end="")
         else:
             print(" ",end="")