'''
        *
      * *
    * * *
  * * * *
* * * * *

'''

n=int(input("enter the num"))

for i in range(1,n+1):
    print()
    for k in range(1,n-i+1):
        print("  ",end="")
    
    for j in range(1,i+1):
        print("* ",end="")
