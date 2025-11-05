# Function that takes a number and return its binary form without using bin() . 

def numberConvertBinary(n):
    binary = "" # For storing binary number
    num=n
    while(n>0):
        r = n % 2
        binary += str(r)
        n = n//2
    print("Binary number of ",num, " is : ",binary[::-1])

num = int(input("Enter a number : "))
numberConvertBinary(num)