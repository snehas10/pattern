"""
EEEEE
DDDD
CCC
BB
A

"""
n=int(input("Enter a num = "))
ch=69
for i in range(1,n+1):
    print()
    for j in range(1, n-i+2):
        print(chr(ch),end="")
    ch-=1
