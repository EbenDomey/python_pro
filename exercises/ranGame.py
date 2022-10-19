import random as rd

random_number = rd.randint(1, 10)
# print(random_number)
# uncomment the line above if u want to see the actual random number
count = 1
maxNumberOfTries = 5
answer = False

while answer == False and count < maxNumberOfTries + 1:
    try:
        t = int(input("Enter a number: "))
    except ValueError:
        print("INVALID INPUT!! ONLY NUMBERS ARE ACCEPTED")
        count += 1
        continue
    if random_number == t:
        answer = True
        print(f"Congratulations you won it took u only {count} tries")
        break
    else:
        answer = False
    count += 1

else:
    print("Sorry, you lose")
