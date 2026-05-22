"""
a
ab
abc
abcd
abcde

"""
n=int(input("Enter a num = "))
for i in range(1,n+1):
    print()
    ch=97
    for j in range(1, i+1):
        print(chr(ch),end="")
        ch=ch+1


            
    
