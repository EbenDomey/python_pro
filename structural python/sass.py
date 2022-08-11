import numpy as np
def Function1():
     x = int(input("Start: "))
     y = int(input("Stop: "))
     z = int(input("Step: "))
     global n1
     n1 = np.arange(x,y,z)
     print(n1)
def Function2():
     x = float(input("Start: "))
     y = float(input("Stop: "))
     z = float(input("Step: "))
     n1 = np.arange(x,y,z)
     print(n1)
print("Please select amongst the following\n A) Whole number Values \n B) Decimal Values ")
selection = input()
while selection !="A" and selection !="B":
     print("Invalid input please try again")
     selection = input()
if selection == "A":
     Function1()
elif selection =="B":
     Function2()