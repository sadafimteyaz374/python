# Check The number is prime or not : 
n = int(input("Enter a number : "))

if(n<=1):
    print("Not prime number ")
else:
    f = 0
    for i in range(2,n):
        if(n%i==0):
            f = 1
            break
if(f == 1):
    print("Not prime number ")
else:
    print("Prime number")