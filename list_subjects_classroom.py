# classroom required for subjects : 
list_subjects = {"python","java","c++","python","javascript","java","python","java","c++","c"}
print("classroom required for subjects : ",len(list_subjects))

# make dictionary using 3 subjects and ask user to enter masks
dict = {}

m1 = input("Enter physics marks : ")
dict.update({"phy" : m1})

m2 = input("Enter chemistry marks : ")
dict.update({"chem" : m2})

m3 = input("Enter math marks : ")
dict.update({"math" : m3})

print(dict)

# store 9 and 9.0 as a separate value and you can use a built in data types : 
list = [9,"9.0"]
print(list)