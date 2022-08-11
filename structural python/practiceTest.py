"""def lesser_of_two_evens(a,b):
    if a and b %2==0:
        if a<b:
            return a
        else:
            return b
    else:
        if a<b:
            return b
        else:
            return a

print(lesser_of_two_evens(2,5))
t=["Apple","Banana"]
print(t[0][0])
def animalCrackers(text):
    t=text.lower()
    a=t.split();
    print(a)
    if a[0][0] ==a[1][0]:
        return True
    return False

print(animalCrackers("Crazy Kangaroo"))


def old_macdonald(str):
    if (len(str)>4):
        return str[0].upper()+str[1:3]+str[3].upper()+str[4:]
    elif (len(str)<4):
        return 0
    return str[0].upper()+str[1:3]+str[3].upper()

print(old_macdonald("mac"))


def master_yoda(str):
    r=str.split()
    text=r[-1]
    i=len(r)-2
    while i>=0:
        text=text+" "+ r[i]
        i-=1
    return text
print(master_yoda("God is a king and a powerful dude"))

def almost_there(a):
    if abs(100-a)<=10 or abs(200-a)<=10:
        return True
    return False

print(almost_there(150))


def laughter(pattern,text):
    r=len(pattern)
    count=0
    for i in range(len(text)):
        q=text[i:i+r]
        print(q)
        if pattern==q:
            count=count+1
    return count

print(laughter('h','hahahah'))


def paper_doll(str):
    text=""
    for i in range(len(str)):
        text=text+str[i]*3
    return text

print(paper_doll("Mississippi"))


def blackjack(a,b,c):
    tot=a+b+c
    r=tot-10
    if tot<=21:
        return tot
    else:
        if a==11 or b==11 or c==11:
            return r
        else:
            return "BUST"
print(blackjack(9,9,11))"""

def summer_69(nums):
    total=0
    count=True
    for i in range(len(nums)):
        if nums[i]==6:
            count=False
        elif count==False and nums[i]==9:
            count=True
        elif count==True :
            total=total+nums[i]

    return total

print(summer_69([2,1,6,9,11]))


def spy_game(nums):
    q=nums.index(0)
    s=nums.index(7)
    w=nums.index(0,q+1)
    if q<w<s:
        return True
    else:
        return False

print(spy_game([1,7,2,0,4,5,0]))

"""count=0
for i in range(2,100):
    j=2
    while j<=i:
        if i%j==0:
            break
        j+=1
    if i==j:
        count=count+1
print(count)"""


def count_prime(nums):
    count=0
    for i in range(2,nums):
        j=2
        while j<=i:
            if i%j==0:
                break
            j+=1
        if i==j:
            count=count+1
    return count


print(count_prime(200))
def print_big(letter):
    if letter=="a":
        print("  *  ")
        print(" * * ")
        print("*****")
        print("*   *")
        print("*   *")
    elif letter=="b":
        print("*****")
        print("*    *")
        print("*****")
        print("*    *")
        print("*****")
    elif letter=="c":
        print(" ** ")
        print("*  *")
        print("*   ")
        print("*   ")
        print("*   ")
        print("*  *")
        print(" ** ")
    elif letter=="d":
        print("****")
        print("*   *")
        print("*    *")
        print("*    *")
        print("*   *")
        print("****")
    elif letter=="e":
        print("*****")
        print("*    ")
        print("*****")
        print("*    ")
        print("*****")

print_big("a")
print("\n")
print_big("b")
print("\n")
print_big("a")