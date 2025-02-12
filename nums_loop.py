# Print the list using loops and search x element :

nums = [1,4,9,16,25,36,49,64,81,100]

#while loop
i = 0
while(i<len(nums)):
    print(nums[i])
    i += 1
print("\n\n\n")
#for loop
for num in nums:
    print(num)

nums = (1,4,9,16,25,36,49,64,81,100)
#while loop
x = 36
i = 0
while(i<len(nums)):
    if(x == nums[i]):
        print("Found at : ",i)
    i += 1
print("\n\n")
#for loop
n = 21
for num in nums:
    if(n == num):
        print("Found ")
    else:
        print("Finding.....")