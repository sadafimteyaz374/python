# Reverse a string using python programs :
str = input("Enter a string : ")
i = len(str)-1
str1 = ""
while(i >= 0):
    str1 += str[i]
    i -= 1
print(str1)

if(str == str1):
    print("Palindrome")
else:
    print("not palindrome")