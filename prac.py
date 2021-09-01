data = ("John", "Doe", 53.44)
print("Hello %s %s. Your current balance is %s. Not much, or is it?" % (data[0], data[1], data[2]))
del data

#Basic_String_Operations
password = "Password"
print(password)
#how many characters does the string have?
len(password)
#show at which position the first "o" is
print(password.index ("o")) 
#count the "s" in the string
print(password.count ("s"))
#print the slice of the string starting at 3 ending at index 6
print(password[3:7])
#3rd character from the end
print(password[3:7])
#[start:stop:step]
print(password[3:7:2])
