"""
    1
   11
  1*1
 1**1
11111

"""
n=int(input("enter a num= "))
for i in range(1, n+1):
    print()
    for j in range(1, n-i+1):
        print(" ",end="")
    for k in range(1, i+1):
        if k==1 or k==i or i==n:
            print("1",end="")
        else:
            print("*",end="")
