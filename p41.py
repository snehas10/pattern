"""
A
BCD
EFGHI
JKLMNOP

"""
n=int(input("Enter a num = "))
k=65
for i in range(1,n+1):
    print()
    for j in range(1, 2*i):
        print(chr(k),end="")
        k+=1