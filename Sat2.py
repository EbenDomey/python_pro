def caught_speeding(speed, is_birthday):
    if is_birthday==True:
        t=speed
        if t<=65:
            return 0
        elif t>=66 and t<=85:
            return 1
        elif t>=86:
            return 2
    else:
        t=speed
        if t<=60:
            return 0
        elif t>=61 and t<=80:
            return 1
        elif t>=81:
            return 2


print(caught_speeding(60, False))
print(caught_speeding(65, False))
print(caught_speeding(65, True))
a=1
b=7
if a+b in range(10,20):
    print(True)
else:
    print(False)
print(abs(a-b))

def love6(a, b):
    t=a+b
    r=abs(a-b)
    if a==6 or b==6 or t==6 or r==6:
        return True
    else:
        return False

"""print(love6(6, 4))
print(love6(4, 5))
print(love6(1, 5))"""

def in1to10(n, outside_mode):
    if outside_mode==True:
        if n<=1 or n>=10:
            return True
        else:
            return False
    else:
        if n in range(1,11):
            return True
        else:
            return False

"""print(in1to10(5, False))
print(in1to10(11, False))
print(in1to10(11, True))"""


def near_ten(num):
    rem=num%10
    if rem<=2:
        if rem in range(3):
            return True
        else:
            return False
    else:
        new=10-rem
        if new in range(3):
            return True
        else:
            return False
print(near_ten(12))
print(near_ten(17))
print(near_ten(19))
