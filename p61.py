"""
    1
   123
  12345
 1234567
123456789

"""
n=int(input("enter the number"))

for i in range(1,n+1):
    print()
    for k in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,i*2):
        print(j,end="")

        