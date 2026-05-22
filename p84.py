'''
    1
   212
  32123
 4321234
543212345
'''

n=int(input("enter the number"))

for i in range(1,n+1):
    print()
    for k in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,i*2):
        print(abs(j-i)+1,end="")