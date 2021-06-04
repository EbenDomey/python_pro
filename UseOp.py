#there are other functions and inbuilt methods which we are to talk about
#first would be the range function.This function is used to generate an array of numbers
myList = list(range(10))
print(myList)
firstTuple = tuple(range(0,10,2))
print(firstTuple)
#it can be iterated through too
for comp in range(5):
    print(comp)
    comp += 1
#sometimes we like to notate the items in a string with its index as well as an iterable
i = 0
for a in "hello world":
    print(f"index{i} is {a}")
    i += 1
#also in such cases where the items are too much to iterate like this
# we can place them in a tuple set using the enumerate function
t = 0
word = "cyanocobalamin"
for a in enumerate(word):
    print(a)
#in such case it comes in a tuple set and it can be unpacked using tuple unpacking
for (a,b) in enumerate(word):
    print(f"index {a} is {b}")

#another function operator is the zip function. This is used to pair up multiple iterables into tuple packs
firstList = [1, 2, 3]
duoList = ['a', 'b', 'c']
compList = list(zip(firstList,duoList))
print(compList)
for g in zip(firstList, duoList):
    print(g)
#tuple unpacking
for index,item in zip(firstList, duoList):
    print(f"{index}:{item}")
#also in-terms of the zip function it only pairs up items if the number of items are equal in all iterables
tryList = [1,2,3,5,6]
comList = ['x','y','z']
print(list(zip(tryList,comList)))