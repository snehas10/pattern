'''
123456789
 1234567
  12345
   123
    1
'''

n=int(input("enter the number"))

for i in range(n,0,-1):
    print()
    for k in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,i*2):
        print(j,end="")
        