# Count vowel and consonent in a string 

a = input("Enter a string : ")
i = 0
v = 0
c = 0
while(i<=len(a)-1):
    if(a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u' or a[i]=='A' or a[i]=='E' or a[i]=='I' or a[i]=='O' or a[i]=='U'):
        v += 1
    else:
        c += 1
    i += 1
print("Numbers of vowels : ",v)
print("Number of consonent : ",c)