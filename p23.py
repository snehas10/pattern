"""
a
bc
d f
g  j
klmno

"""
n=int(input("Enter a num = "))
ch=96
for i in range(1, n+1):
    print()
    for j in range(1, i+1):
        if j==1 or j==i or i==n:
            ch+=1
            print(chr(ch),end="")
        else:
            print(" ",end="")