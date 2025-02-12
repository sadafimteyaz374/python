#while loop
n = int(input("Enter a number : "))
sum = 0
i = 0
while(i<=n):
    sum += i 
    i += 1
print("Sum of ",n," : ",sum)

#for loop
sum = 0
x = int(input("Enter a number : "))
for j in range(1,x+1,1):
    sum += j
    j += 1
print("Sum of ",x," : ",sum)