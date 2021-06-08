def evenComp(a,c):
    if a%2==0 and c%2==0:
        return min(a,c)
    else:
        return max(a,c)
print(evenComp(16,4))
print(evenComp(19,5))

def animalCrackers(str):
    ty = str.split()
    f = ty[0]
    g = ty[1]
    if f[0]== g[0]:
        return True
    else:
        return False
print(animalCrackers("Lam Teo"))
#level one
def OldMacDonald(name):
    t = name[0].upper()
    p = name[3].upper()
    print(t+name[1:3]+p+name[4:])
OldMacDonald("samson")

def masterYoda(state):
    g = state.split()
    y = g[::-1]
    p = ""
    for u in y:
        p=p+u+" "
    print(p)
masterYoda("Are you sure")
#level 2
def paperDoll(trot):
    p = ''
    for t in trot:
        p=p+(t*3)
    print(p)

paperDoll("livinglegend")

def Laughter(pattern,text):
    if pattern in text:
        print(text.split(pattern))
Laughter("hah","hahahaha")

def BlackJack(a,b,c):
    myList = [a,b,c]
    u = sum((a,b,c))
    if 11 in myList and u > 21:
        print(u - 10)
    elif u > 21:
            print("BUST")
    if u<=21:
        print(u)
BlackJack(5,6,7)
BlackJack(9,9,9)
BlackJack(9,9,11)

def Summer69(secList):
    i = 0
    for a in secList:
        if a in [6,7,8,9]:
                continue
        i= i + a
    print(i)
Summer69([2, 1, 6, 9, 11])

"""def listToString():
    integer=""
    integer.join()
    t= int(integer)
    return t"""

def spyGame(thirdList):
    print(thirdList.sort())
    if (0,0,7) in thirdList:
        return True
    else:
        return False
print(spyGame([1,2,4,0,0,7,5]))
print(spyGame([1,7,2,0,4,5,0]))
