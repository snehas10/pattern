'''
5 5 5 5 5
 4 4 4 4
  3 3 3
   2 2
    1
'''

n=int(input("enter the number :"))


for i in range(n,0,-1):
    print()
    for k in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,i+1):
        print(i,end=" ")
        
