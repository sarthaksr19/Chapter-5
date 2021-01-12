myDict = {
    "CSE": "Computer Science and Engineering",
    "NAME": "Sarthak Singh",
    "YEAR": [2019],
    1: 2
}
# dictionary methods

print((myDict.keys())) #print the keys of the dictionary in the form of list
print((myDict.values())) #print the values of the dictionary in the form of list

print((myDict.items())) # returns the pair(keys:value) in the form of tuples through the list
print(myDict)

updateDict = {
    "Divyesh": "Friend",
    "Aman": "Friend"
}

myDict.update(updateDict) #update the dictionary key-value from the updateDict.
print(myDict)

# difference between .get and [] syntax in dictionaries?

print(myDict.get("CSE1")) #return None as CSE1 is not available in the dictionary
print(myDict['CSE1'])       #throws an error as CSE1 is not available in the dictionary

