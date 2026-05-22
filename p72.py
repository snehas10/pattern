'''
A B C D E
 A B C D
  A B C
   A B
    A
'''
n=int(input("enter the number :"))


for i in range(n,0,-1):
    print()
    for k in range(1,n-i+1):
        print(" ",end="")
    ch=65
    for j in range(1,i+1):
        print(chr(ch),end=" ")
        ch+=1