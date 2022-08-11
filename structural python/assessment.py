t = "hello"
print(t[::-1])
list3 = [1,2,[3,4,'hello']]
myList = list3[2]
print(myList)
myList[2]="goodbye"
print(myList)
print(list3)
list4 = [5,3,4,6,1]
list4.sort()
print(list4)
dict1 = {"k1": "hello"}
print(dict1['k1'])
dict2 = {"k1": {"k2":"hello"}}
perDict = dict2['k1']
print(perDict['k2'])
dict3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
subList1 = dict3['k1']
subDict1 = subList1[0]
subList2 = subDict1['nest_key']
subList3 = subList2[1]
print(subList3[0])
dict4 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
divList1 = dict4['k1']
divDict1 = divList1[2]
divList2 = divDict1['k2']
divDict3 = divList2[1]
divList4 = divDict3['tough']
divList5 = divList4[2]
print(divList5[0])

list5 = [1,1,2, 2, 33, 4, 4, 11, 22, 3, 3, 2]
mySet = set(list5)
print(mySet)
print(3.0==3)
print(4.0*0.5==2)

finList = [1,2,[3,4]]
finDict = [1,2,{'k1':4}]
print(finList[2][0]>= finDict[2]['k1'])