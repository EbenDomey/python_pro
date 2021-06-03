# like we said loops can be used for all iterables in this case we talk about tuples
firstTup = ((1, 2), (3, 4), (5,6))
for a in firstTup:
    print(a)

#for getting each and every value in the tuple we have to unpack them
secTup = ((1,2), (3,4), (5,6))
for (a,b) in secTup:
    print(f"{a} \n{b}")
#this also works for three set nested tuple
thirdTuple=((2,4,6),(1,3,5),(7,9,0))
for (c,d,e) in thirdTuple:
    print(f"\n{c} \n{d} \n{e}")

#for dictionaries
firstDict = {'k1':1,'k2':2, 'k3':3}
#to loop through this
for items in firstDict:
    print(items)
# this will only return the keys only but for both
for ite in firstDict.items():
    print(ite)
# this will make it print both keys and values in tuple pairs
# thus to print specific we can use methods .value(),.key() or tuple unpacking

#.value assuming we only want values
for ita in firstDict.values():
    print(ita)

#for tuple unpacking
for key,value in firstDict:
    print(value)
# that is it for for loops onto the next one!