"""
A
AB
ABC
ABCD
ABCDE

"""
n=int(input("enter a num = "))
for i in range(1, n+1):
    print()
    ch=65
    for j in range(1, i+1):
       print(chr(ch),end="")
       ch=ch+1
