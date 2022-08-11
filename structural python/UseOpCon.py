#another functionality is the 'in'
#this is used to discover if an item is a part of a whole
#in a list..
myList = list(range(1,10,2))
print(9 in myList)
# in a dictionary
myDict = {'k1':356}
print('k2' in myDict)
#using dictionary method
print(356 in myDict.values())
#in strings
myString = "benzole sodium"
print('benzole' in myString)

#another are the arithmetic functions like max and min
#max is used to determine a large quantity in a list or set
anotherList = list(range(10,100,10))
print(max(anotherList))
#min is used to determine the less quantity
print(min(anotherList))

#we are about to use a python library for the first time its name is random
#we'd like to shuffle lists and randomize list items
from random import shuffle
iterList = list(range(10))
shuffle(iterList)
print(iterList)
#if we try to assign this iteration method to a variable it would return nothing because
# this function allows change but cannot assign change
sitList = shuffle(iterList)
print(sitList)#returns nothing

#in the random library are other objects like randint
from random import randint
print(randint(0,100))
#this function can be assigned a variable
Shu = randint(10,1000)
print(Shu)


#another method is the input method this is use to take user input and store as data
idea = input("What is the best idea ever made:\n")
edit = idea.upper()
print(f"'{edit}' is a good one")
#this can be used to take in values in string form but this value can later be cast into a float or integer
inp = input("How many times is 4 equals 24:\n")
con = int(inp)
print(f"{con} is correct!")
#this ends useful operators in python on to the next