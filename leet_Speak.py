aString = input("Enter a string to translate: ")
# aString = "Kate"
leet1 = ["A", "E", "G", "I", "O", "S", "T"]
leet2 = [4,3,6,1,0,5,7]
index = 0
newString = " "
while index < len(aString): 
    char = aString[index].upper()
    y = 0
    while y < len(leet1): 
        if char == leet1[y]:
            char = str(leet2[y])
        y += 1
    newString += char
    index += 1 
   
print (newString)
    




