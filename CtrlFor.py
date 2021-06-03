#Now we go to a different variation of Control Flow; Looping
#We Start With For Loop
#Almost all objects in python are iterables (they can be manipulated) for that matter all loop kinds can be used on them
#for list
myList = [1,2,3,4,5,6]
for num in myList:
    print(num)

#Also all contents in an iterable can be used to print other stuff
for con in myList:
    print("Hey")

#Also you can introduce your content with a string
for can in myList:
    if can %2 ==0:
        print(f"Even number: {can}")
    else:
        print(f"Odd Number: {can}")
#You can also find the sum and recursion with said loop
pioSum = 0
for van in myList:
    pioSum= pioSum + van
    #print(pioSum)#This will return cumulative values
print(pioSum) #Prints final value only

#You can also iterate a string as well
Name = "Van Helsing"
for a in Name:
    print(a)
yam = Name.upper()
for b in yam:
    print(b)

#just like lists and other iterables strings can also be looped with different statements whose number of times of appearance is known
for v in Name:
    print("I'm right")
