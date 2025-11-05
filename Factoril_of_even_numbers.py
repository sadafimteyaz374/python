#Function that returns the factorial of even numbers only

def factorial(n):
    f = 1
    for i in range(1,n+1):
        f = 1
        if(i%2==0):
            for j in range(1,i+1):
                f *= j
            print("Factorial of ",i," : ",f)

num = int(input("Enter a number : "))
factorial(num)