"""
1
10
1 1
1  0
10101

"""
n=int(input("enter a num = "))
for i in range(1, n+1):
    print()
    for j in range(1, i+1):
        if j==1 or (j==i and i%2!=0):
            print("1",end="")
        elif i==n:
            if j%2!=0:
                print("1",end="")
            else:
                print("0",end="")            
        elif j==i//2+1 and i%2==0:
            print("0",end="")
        else:
            print(" ",end="")
