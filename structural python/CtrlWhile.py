#while loops are loops that function by continually running a code until its condition is satisfied
a = 0
while a < 5:
    print(a)
    a += 1
#an else statement can be used incase the original code isn't satisfied in a way
else:
    print("Sorry this value is not less than five")
#now we are about to learn about break,continue, and pass statements
# the pass statements tells a loop to do nothing at all
# this comes in handy when you want to include something that hasn't come to mind yet. This works better with for loops
myList = [1,2,3,4,5]
for t in myList:
    pass
print("This is the end of my codebase")
#the continue statement is used to skip over a currently looping item assuming it has been conditioned
for g in myList:
    if g %2 == 0:
        continue
    print(f"Odd numbers: {g}")
#this also works for while loops
b = 0
"""while b < 6:
    if b==4:
        continue
    print(b)
    b+=1

#the break statement is used to stop a looping from occuring assuming that immediate item has been conditioned
for y in myList:
    if g == "3":
        break
    print(y)"""
#this also functions in while loops
while b<6:
    if b == 4:
        break
    print(b)
    b+=1