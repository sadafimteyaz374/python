# Function that counts how many palindrome words are in a sentence

def checkPalindrome():
    count = 0
    f = open("sentence.txt","r")
    data = f.read()
    print(data)

    words = data.split()

    for word in words:
        if(word == word[::-1]):
            print("Palindrome word is : ",word)
            count = count + 1
    
    print("Number of Palindrome word in given sentence : ",count)

checkPalindrome()