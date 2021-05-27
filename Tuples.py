#These are iterables that function just like lists but are denoted syntactically by parentheses
firstTuple=("name", 15)
print(firstTuple)
#These iterables are immutable(Their contents in relation to their index cannot be reassigned)
#firstTuple[2]=0
#print(firstTuple[2]) returns TypeError

#Like lists the contents of these iterables can be called unto and number of contents can be named
print(firstTuple[0])
len(firstTuple)
#The number of occurrences of an item in tuple can be discovered with the count method
secTup=('a', 'a', 'c')
print(secTup)
print(secTup.count('a'))
#The index position of an item in a tuple can be discovered using the index method
print(secTup.index('c'))
#Technically tuples aren't of relevance to a beginner python programmer to an advanced however it can be used to create data integrity systems in which the information cannot be changed