'''
        A
      A B
    A B C
  A B C D
A B C D E  

'''

n=int(input("enter the num"))


for i in range(1,n+1):
    print()
    for k in range(1,n-i+1):
        print("  ",end="")
    ch=65
    for j in range(1,i+1):
        print(chr(ch),end=" ")
        ch+=1