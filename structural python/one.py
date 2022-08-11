scorpion = ("Walter","Toby","Happy","Sylvester","Paige")
scorpion2 = list(scorpion)
scorpion2.append("Gallo")
scorpion = tuple(scorpion2)
print(scorpion)

fruits = ("Apple","Banana","Guava","Cherry")
(red,yellow,green,pink) = fruits
print(pink,green,yellow,red)

#We are going on ahead to learn sets which have no order or index
firstSet = {"Helena","Jessie","Cwesi","Estelle",2018,2015,2013,2014}
print(firstSet)
firstSet.add("Jeshurun")
print(firstSet)
Songs = ["World","Healing Stream","Teach me the way",2018]
Albums = ("Relapse","Recovery","Revival","Music to be murdered")
print(firstSet)
firstSet.symmetric_difference_update(Songs)
print(firstSet)

#Next and final is Dictionaries
firstDict = {
     "Name" : "Ebenezer Domey",
     "Age" : 17,
     "Location" : "Adenta New-Site"
}
print(firstDict)
r = firstDict.get("Name")
print(r)
x = firstDict.keys()
print(x)
firstDict["Date of birth"] = "10th May 2003"
print(x)
mydict = firstDict.copy()
print(mydict)
#We go ahead to learn nested dictionaries
myFamily = {
     "child1":{
          "name" : "Esther",
          "year of birth" : 1992
     },
     "child2" : {
          "name" : "Benjamin",
          "year of birth" : 1999
     },
     "child3" : {
          "name" : "Ebenezer",
          "year of birth" : 2003
     }
}
print(myFamily)
#There is another type of approach
child1 = {
     "name" : "Ebenezer",
     "year" : 1234
}
child2 = {
     "name" : "Eren",
     "year" : 5641
}
child3 = {
     "name" : "Aaron",
     "year" : 6512
}
myFamily2 = {
     "child1" : child1,
     "child2" : child2,
     "child3" : child3
}
print(myFamily2)

# So we are done with an annoying piece of python on to the next shall we
a = 70
b = 35
if a > b :
     print("Well lucky you You haven't failed yet")
elif a==b :
     print("Sorry this try is a discarded one you understand")
else :
     print("Oh no this is bad for you better luck next time")
#That is it for this python file folks byeee