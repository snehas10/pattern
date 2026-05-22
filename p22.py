"""
A
AB
A C
A  D
ABCDE

"""
n=int(input("Enter a num = "))
for i in range(1, n+1):
    print()
    for j in range(1, n+1):
        ch=64+j
        if j==1 or j==i or i==n:
            print(chr(ch),end="")
        else:
            print(" ",end="")
            ch+=1