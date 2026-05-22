"""
    A
   AB
  ABC
 ABCD
ABCDE

"""
n=int(input("Enter a num="))
for i in range(1, n+1):
    print()
    for j in range(1, n-i+1):
        print(" ",end="")
    ch=65    
    for k in range(1, i+1):
        print(chr(ch),end="")
        ch=ch+1    

