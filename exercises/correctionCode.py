try:
    t = int(input("Input your number: "))
except ValueError:
    print("INVALID INPUT!!!NUMBERS ONLY")
    exit()

print(f"your number is {t}")
