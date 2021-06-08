#Nested statements are statements that exist in other statements
"""a = 4
if a <=5:
    if a==4:
        print("This is a less even number")"""
#Statements are basically functions and its associated conditions
#Scope refers to the range in which a variable or a function can work
name = "Tyler"
def hello():
    name= "Ebenezer" #its scope is only in this function thus doesn't function globally
    print(f"Hi my name is {name}")
print(name)
#if we wanna call the local one we have to call the function
hello()
"""
    Python Uses a method known as "LEGB" in calling variables
    L: Local. This means that before it calls the outer namespace it would check the inner function
    E: Enclosing function. This refers to the variable inside the pioneer function
    in terms of a nested function
    G: Global. Python calls on the global namespace if the above aren't available
    B: Built in function. This means python can overwrite an in built function if it has been defined
    another way.
"""
#Sample code block
#place comment symbol on each variable and run to see the effects
age = 10 # global is called last
def FiveYears():
    age = 15# Enclosing is called second
    def tenYears():
        age = 25# local is called first
        print(f"You are {age} years old")
    tenYears()
FiveYears()

#the following must be avoided no matter what but if you do it no fears just erase and restart kernel
"""
    def len(var):
        return count(var)
    print(len(25)) representing built-in. Do not run this no matter what
"""
#to make a local function a global one u have to declare with the global keyword
print(age)
def test():
    #global age you don't necessarily have to do this
    # It makes it impossible to reassign the same variable. there is a hack
    age = 25
    print(f"Age has been changed to {age} globally")
test()
print(age)
"""#hack
def tester(age):
    age = 50
    print(f"{age} is age")
    return age
age = tester(age)
print(tester(age))
print(age)"""