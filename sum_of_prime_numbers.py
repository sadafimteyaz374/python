#function that returns sum of prime numbers up to n

def isPrime(n):
    if(n<2):
        return False
    for j in range(2, n):
        if(n%j==0):
            return False
    return True

def sumOfPrime(n):
    s = 0
    for i in range(2,n+1):
        if isPrime(i):
            s=s+i
    return s

n = int(input("Enter a number : "))
print(sumOfPrime(n))