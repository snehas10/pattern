'''
123456789
 1+++++7
  1+++5
   1+3
    1
'''
n=int(input("enter the number"))

for i in range(n,0,-1):
    print()
    for k in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,i*2):
        if i==n:
           print(j,end="")
        elif j==1:
           print(j,end="")
        elif j==i*2-1:
           print(j,end="")
        else:
           print("+",end="")
