#functions are used to define a code block you can call for anytime
def firstFunc():
    print("Hello world")
firstFunc()
#you can include a parameter(argument) into the parenthesis of a defining function
#you can also include a default assignment to the paranthesis for error handling
def secFunc(name="Eben"):
    """
    this is used to create an info block for the code written in the function
    """
    print("hello "+name)
#this default value can be overwritten by calling the function with a new function
secFunc()
secFunc("Rex")
#sometimes a function cannot be assigned a variable because there is a direct function running in it
#to fix that you have to use the return keyword that will guarantee assignment
def thirdFunc(lName):
    return f"hello {lName} pleasure to meet"
show = thirdFunc("Domey")
print(show)
#another
def dog_type(animal):
    #can also be written as
    return "dog" in animal.lower()
    """
    if 'dog' in animal.lower():
        return True
    else:
        return False"""
type =input("Animal Name: ")
print(dog_type(type))


#let's do something challenging
#let's create pig latin which is word rearranging to produce a security keyword of some sort
"""
    the aim is to take a word
    if the word starts with a vowel 'ay' is added to the end
    if the word starts with a consonant then the first letter is moved to the last and 'ay' is added
    """
def pigLatin(word):
    #call upon the first letter in the word
    t = word[0]
    #declare an if statement concerning vowel t or consonant t
    if t in "aeiou":
        pigLatin = word+"ay"
    else:
        pigLatin = word[1:] + t + 'ay'
    return pigLatin
print(pigLatin("tree"))