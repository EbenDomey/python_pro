class Animal():
    def __init__(self):
        print("Animal created!")
    def eat(self):
        print("Animal eat!")
    def walk(self):
        print("Animal walk!")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created!")
    def bark(self):
        print("Dog bark!")
    def eat(self):
        print("Dog eat!")

class Cat(Dog):
    def __init__(self):
        Animal.__init__(self)
        print("Cat created!")
    def meow(self):
        print("Cat meow!")
    def eat(self):
        print("Cat eat!")


myDog = Dog()
myDog.eat()
myCat = Cat()
myCat.eat()