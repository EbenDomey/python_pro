import math
from collections import Counter
import string
def vol(rad):
    volume = (4/3)*math.pi*(rad**3)
    return volume
r= vol(3)
print(f"the result is {r} but to 1d.p it's {r:1.1f}")

#num 2
def ranCheck(num,low,high):
    if num in range(low,high):
        print(f"Yup {num} is present in range {low} to {high}")
ranCheck(5,1,10)
#alternative
def Rancheck(num,low,high):
    return num in range(low,high)
print(Rancheck(3,1,10))

#num 3
def upLow(str):
    upd=0
    lowd=0
    for x in str:
        if x.isupper():
            upd+=1
        elif x.islower():
            lowd+=1
        else:
            pass
    print(f"uppercase:{upd}\nLowercase:{lowd}")
upLow("Hello Mr. Rogers, how are you this fine Tuesday")

#alternative
"""def up_low(s):
    c = Counter(s)
    print(c)
    t= sum(c.values)
    print(t)
up_low("Hello Mr. Rogers, how are you this fine Tuesday")"""

#num 4
def UniqueList(l):
    t = set(l)
    g =list(t)
    print(g)
r = [1,1,1,1,1,1,1,2,2,2,3,3,4,4,5,5,5]
UniqueList(r)

#num 5
def multiply(numbers):
    g = 1
    for t in numbers:
        g= g*t
    print(g)
myList = [1,2,3,-4]
multiply(myList)

#num 6
def palindrome(word):
    return word == word[::-1]
print(palindrome("madam"))

#num7
"""
    We have to make alphabets into sets as well as the string sentence
    so that if the number of characters in that string is less than the ones in the alphaset
    it would return false else true
"""
def ispanagram(sent,alphabet = string.ascii_lowercase):
    alphaset = set(alphabet)
    return len(alphaset)<=len(set(sent))
"""for c in sent.lower():
        if c in alphabet:
            return True
        else:
return False"""
print(ispanagram("The quick brown fox jumps over the lazy dog"))