"""
ABCDE
ABCD
ABC
AB
A

"""
n=int(input("Enter a num = "))
for i in range(1, n+1):
    print()
    ch=65
    for j in range(1, n-i+2):
        print(chr(ch),end="")
        ch+=1
        