#Lambda expressions are functions that are not defined and are also called once
#Before we talk about that we have to talk about map and filter
#the map function is used to iterate through a list with a function designated for a single value
def squareRoot(num):
    return num**0.5
#the map function cannot be called directly. It must be added to a list
myList=[4,9,16,25,36,49,64]
newList= list(map(squareRoot,myList))
print(newList)
# Or iterated through with a loop
"""for items in newList:
    print(items)

t = 0
i = 0
while t<=6:
    print(newList[i])
    i+=1
    t+=1"""
#for iterations in a string
def stringman(str):
    if len(str)%2==0:
        return str[:2]
    else:
        return str[0]

myListstr = ["Andy","Irene", "Orion", "Nancy"]

con = list(map(stringman,myListstr))
print(con)

y = 0
u = 0
"""while y<=4:
    print(myListstr[u])
    u+=1
    y+=1"""


#up next filter. This function returns the value of a function which is meant to return a boolean
def evenTest(nums):
    return nums%2==0

numList = list(range(1,11))
novList=list(filter(evenTest,numList))
print(novList)
