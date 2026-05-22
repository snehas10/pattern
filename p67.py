'''
    A
   B B
  C   C
 D     D
EEEEEEEEE
'''

n=int(input("enter the number"))
ch=65

for i in range(1,n+1):
    print()
    for k in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,i*2):
        if j==1:
            print(chr(ch),end="")

        elif i==n:
            print(chr(ch),end="")

        elif j==i*2-1:
            print(chr(ch),end="")
        else:
            print(" ",end="")
    ch+=1
        