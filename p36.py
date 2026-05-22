"""
ABCDE
A  D
A C
AB
A

"""
n=int(input("Enter a num = "))
for i in range(1, n+1):
    print()
    for j in range(1, n+1):
        if j==1 or i==1 or i+j==n+1:
            print(chr(65 + j - 1),end="")
        else:
            print(" ",end="")
