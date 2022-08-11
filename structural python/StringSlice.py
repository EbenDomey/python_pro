mystring = "abcdefghijkl"
print(mystring[3:10])

#let's see if the assignment operations would work for strings
t = "Hello"
t+= " its nice to meet you"
print(t)
#well people it works
r = "Rotten tomatoes"
r.upper()
gt = "Helping meing pleaseing people"
print(gt.split("ing"))
#formatting strings with print
print("This is a silly {0} {1} {2}".format("waste", "of", "time"))
#representing with variables
print("The {q} {b} {f} jumped over the {l} {d}".format(q="quick", b="brown", f="fox", l="lazy", d="dog"))
#using this for floating point values and rounding
result = 100/777
print(result)
print("Therefore the result is {}".format(result))
#to three dp
print("To three dp it is {r:2.3f}".format(r=result))
#lists are sort of python arrays which are ordered(They are not randomized) and allow mutability(its content can be changed)
firstList = [1,2,3]
stringList= ["apple","banana", "guava"]
hybridList= ["apple", 2, 5.36]
print(f"{firstList}, {stringList}, {hybridList}")
#this iterable can be concatenated and supports many methods
newList= firstList + stringList
print(newList)
#in terms of mutability
newList[0]= "Extra Terrestrial"
print(newList,newList[-1])
#this iterable can be sliced
print(newList[2::2])
#this iterable can have its content sorted reversed and it contents can be appended or removed(this removal can be specified by index position)
alphaList=["a","g","i","o","y"]
numList=[5,9, 3, 2, 7, 18]
alphaList.append("c")
numList.append(17)
alphaList.sort()
print(alphaList)
numList.sort()
print(numList)
alphaList.reverse()
print(alphaList)
numList.reverse()
print(numList)
alphaList.pop(2)
print(alphaList)
numList.pop(5)
print(numList)