#Sets are unordered collection of unique items
firstSet = set()
print(firstSet)
#They are syntactically denoted with parentheses but unlike a dictionary it does not include key-value pairs
#You add items to a set with the add method
firstSet.add(1)
firstSet.add(2)
print(firstSet)
#Basically as of the unique feature this means multiple kind of item can be placed into a set but only one of it can be displayed
secSet={1, 2, 3, 2, 3 , 1}
print(secSet)
#They also cannot be named by index since they are unordered
#Any set can be created through casting
myList = ["apple", "banana", 5, 25.3, "apple", "banana", 5]
print(myList)
thirdSet=set(myList)
print(thirdSet)
#As of now Sets are not important but we'll dive into that later