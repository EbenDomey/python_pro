"""
#number 1
for a in ['a', 'b', 'c', 'd']:
    try:
        print(a**2)
    except TypeError:
        print("Operation is not allowed on the defined list")
        break
    finally:
        print("Thanks for understanding")


#number 2

x=5
y=0
try:
    z=x/y
except ZeroDivisionError:
    print("Division by zero is an illogical operation")
finally:
    print("All done!")

"""
#number 3
def ask():
    while True:
        try:
            x=int(input("Enter a number: "))
        except ValueError:
            print("An error occurred! Please try again")
        else:
            print("Alright, your square number is: ", x**2)
            break

ask()