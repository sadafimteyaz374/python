# multilication table using n number
print("Using while loop multiplucation table : ")
n = int(input("Enter a number : "))
i = 1
while(i<=10):
    print(n*i)
    i+=1

print("\nUsing for loop multiplication table : ")
x = int(input("Enter a number : "))
for i in range(1,11):
    print(x*i)