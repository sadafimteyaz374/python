n = int(input("Enter a number : "))
n1 = n
sum = 0
while(n>0):
    r = n % 10
    sum += r
    n = n // 10
print("Sum of digit of ", n1 ," : ",sum)