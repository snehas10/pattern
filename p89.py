'''
     1               
    101            
   10101         
  1010101           
 101010101 
10101010101
'''

n=int(input("enter the number"))

for i in range(1,n+1):
    print()
    for k in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,i*2):
        if j%2==0:
            print("0",end="")
        else:
            print("1",end="")
