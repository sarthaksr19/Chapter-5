b = set()

b.add(4)
b.add(5)
b.add(5)  
b.add(5) 
b.add((5,6,8,9))  #sets adds tuples but not list as lists are mutable
# b.add({4:5}) #as like list we cannot implement dictionaries in set

print(b)

print(len(b)) #prints the length of sets

b.remove(5) #remove 5 from the set b and then print the reamining b sets value

print(b.pop()) #pop some random value of set b and return

print(b.clear()) #it clears all bthe value of the list and return none

print(b)


