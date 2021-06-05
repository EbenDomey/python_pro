#sometimes when u create an arithmetic function and u cant anticipate user input it becomes an issue
def percent(a,b,c=0,d=0,e=0):
    """to return ten percent of a total"""
    return sum((a,b,c,d,e))*0.1
print(percent(50,100,50,120))
#that's why the args and kwargs(keywordArguments) are introduced
#its okay to represent them with any name but they must always be denoted by *(args) and **(kwargs)
#this is for code readability by a third-person
#the *args can be used to define multiple(arbitrary number) numerical arguments without writing more arguments

def percent2(*args):
    return sum(args)*0.01
print(percent2(10,15,25,64,108))

#they can also be iterated upon
def multi(*star):
    for a in star:
        print(a)
multi(1,2,3,40,56,91)

#moving to *kwargs
#these are used to iterate over multiple string arguments without passing each in the define block
#**kwargs are designed to return a dictionary of arbitrary arguments
def favFood(**kwargs):
    if 'food' in kwargs:
        print(f"My favorite food to eat is {kwargs['food']} and I like it with {kwargs['drink']}")
    else:
        print("That is not a food!")
favFood(food= 'goat casserole', drink="aloe vera juice")
#combining *args and **kwargs
def favCom(*args,**kwargs):
    print(args)
    print(kwargs)
    print(f"I want {args[0]} pieces of {kwargs['food']}")
    #as we know the *args returns arbitrary tuples whiles the **kwargs returns an arbitrary dictionary
favCom(10,20,30,40,food = 'Egg',fruits='orange',clothes='gucci')