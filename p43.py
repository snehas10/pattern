"""
      1
     12
    123
   1234
  12345
"""
n=int(input("Enter a num = "))
for i in range(1, n+1):
    print()

    for j in range(1, n-i+2):
        print(" ",end="")
        
    for k in range(1, i+1):
        print(k,end="")
