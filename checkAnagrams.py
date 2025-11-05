# Function that checks wheather two strings are anagrams ( eg. listen , silent)

def checkAnagram(str1, str2):
    
    #remove space and lowercase
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()

    if(sorted(str1) == sorted(str2)):      #Sorted sort the string
        print("It is an anagram")
    else:
        print("It is not an anagram")
    

str1 = input("Enter a string : ")
str2 = input("Enter a string : ")

checkAnagram(str1, str2)
