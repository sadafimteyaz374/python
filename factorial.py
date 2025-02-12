# factorial of n numbers :

# while loop
n = int(input("enter a number : "))
fact = 1
i = 1
while(n>=i):
    fact *= i 
    i += 1
print("Factorial : ",fact)

# For loop 
x = int(input("Enter a number : "))
fact1 = 1
for i in range(x,0,-1):
    fact1 *= i
    i += 1
print("Factorial : ",fact1)