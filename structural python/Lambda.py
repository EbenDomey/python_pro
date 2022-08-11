#moving on to lambda
#this is a function known as "The anonymous function". this is because a lambda function
#is only called once and so it doesn't require a name or the def keyword
# those are just replaced with lambda
cubeRoot=lambda num: num **(1/3)
print(cubeRoot(81))
oddList = [8,27,64,125,276]
trial = list(map(cubeRoot,oddList))
print(trial)
splicer = lambda str: str[0]
strList=["Adam","Daniel","Aaron","Margaret"]
print(list(map(splicer,strList)))
#filter Lambda
oddFish = lambda nums: nums%2!=0
evenStr = lambda name: len(name)%2!=0
genList = list(range(0,12))
trial2 = list(filter(oddFish,genList))
print(trial2)
print(list(filter(evenStr,strList)))
