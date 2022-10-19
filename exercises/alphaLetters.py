def up_low(s):
    myDict = {'upper':0, 'lower': 0}
    for letter in s:
        if letter.isupper():
            myDict['upper'] += 1
        else:
            myDict['lower'] += 1
    print(f"Upper case letters: {myDict['upper']}")
    print(f"Lower case letters: {myDict['lower']}")

up_low("Hello how are you?")