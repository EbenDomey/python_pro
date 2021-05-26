#second iterable is dictionary
#these are iterables that are unordered that is they cannot be indexed sorted or sliced in any way
firstDict={"name": "Ebenezer"}
#firstDict[0] throws key error
#but they can be called by their keys
firstDict["name"]
#and can be mutated through this way
firstDict["name"]="Gavin Belson"
firstDict["name"]
#their main syntax is denoted by {} and in them are key:value pairs separated by commas
secondDict={"movie":"Fast and Furious", "genre": "action", "debut year":"2000"}
print(secondDict)
#these can be nested (they can contain lists, tuples and strings integers and floating points)
thirdDict ={"series": "iZombie","genre":("horror", "sci-fi"), "seasons":[11, 2, 31, 14, 5],"Actors":["Liv Moore", "Clive Babineaux", "Peyton Charles"], "ratings": 5.5}
print(thirdDict)
#these nested iterables can be called upon and iterated how they are known to be able to
print(thirdDict["seasons"], thirdDict["genre"])
myList = thirdDict["Actors"]
print(myList)
Letter = myList[-1]
print(Letter.upper())
#this also contains methods that aid in function
print(thirdDict.keys())#for viewing keys
print(thirdDict.values())#for viewing values
print(thirdDict.items()) #for viewing both keys and values in list structure