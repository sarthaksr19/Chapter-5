myDict = {
    "kitaab": "books",
    "darwaaza": "door",
    "bartaan": "utensils"
}
print("your hindi words are ", myDict.keys())
a = input("enter your hindi word: ")

# print("the meaning of your word is ", myDict[a)]

# below line will return none value if keys doesn't match with a user input.

print("the meaning of your word is ", myDict.get(a))
