"""
*****
####
***
##
*

"""
n=int(input("Enter a num = "))
for i in range(1, n+1):
    print()
    for j in range(1, n-i+2):
        if i%2==0:
            print("#",end="")
        else:
            print("*",end="")
