'''
    A
   ABC
  ABCDE
 ABCDEEF
ABCDEFGHI

'''
n=int(input("enter the number"))

for i in range(1,n+1):
    print()
    ch=65
    for k in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,i*2):
        print(chr(ch),end="")
        ch+=1
