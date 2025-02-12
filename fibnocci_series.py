# Fibnocci series :

num = int(input("Enter a range of numbers : "))
i = 0
n = 0
n1 = 1
print(n,"\n",n1)
r = n + n1
while(i<=num):
    print(r)
    n = n1
    n1 = r
    r = n + n1
    i += 1