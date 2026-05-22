"""
123456
54321
1234
321
12
1

"""
n=int(input("Enter a num = "))
for i in range(1, n+1):
    print()
    for j in range(1, n-i+2):
        if i%2==0 and i==2:
            print(n-j+1,end="")
        elif i%2==0 and i!=2:
            print(n-j-2,end="")
        else:
            print(j,end="")