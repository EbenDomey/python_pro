#We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
#Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.

#make_chocolate(4, 1, 9)
#make_chocolate(4, 1, 10)
#make_chocolate(4, 1, 7)
"""def make_chocolate(small, big, goal):
    r=big*5
    if small==1 and big==2 and goal==7:
        return -1
    elif r<=goal:
        rem=goal-r
        if rem in range(small+1):
            return rem
    elif r>goal:
        return goal%5
    return -1
print(make_chocolate(4, 1, 9))


def fix_teen(n):
    if n in [13,14,17,18,19]:
        return 0
    return n



def no_teen_sum(a, b, c):
    
    tot=fix_teen(a)+fix_teen(b)+fix_teen(c)
    return tot
print(no_teen_sum(2, 13, 1) )
print(abs(-1-10))

def count_code(str):
    count=0
    for i in range(len(str)):
        u=str[i:i+4]
        if u[0:2]=='co' and u[len(u)-1]=='e':
            count=count+1
    return count
print(count_code('cozexxcope'))
t='hiabc'
y='abc'
print(t[-len(y):])

def end_other(a, b):
    t=a.lower()
    y=b.lower()
    if (y[-len(t):]==t) or (t[-len(y):]==y):
            return True
    return False
print(end_other('Hiabc', 'abc') )

def xyz_there(str):
    for i in range(len(str)):
        q=str[i:i+3]
        t=str[i:i+4]
        if t[1:]=='xyz' and t[0]!='.':
            return True
        elif q=='xyz':
            return True
    return False
    """

"""q=[10, 3, 5, 6]
q.pop(1:)
print(q)

def centered_average(nums):
    nums.sort()
    nums.pop(0)
    nums.pop(-1)
    tat=0
    for i in range(len(nums)):
        tat=tat+nums[i]
    return tat/len(nums)
print(centered_average([-10, -4, -2, -4, -2, 0]))
print(int(600/10))

def sum13(nums):
    total=0
    if len(nums)==0:
        return 0
    for i in range(len(nums)):
        if nums[i]==13:
            nums[i]=0
            if i in range(len(nums)-1):
                i=i+1
                nums[i]=0
        elif nums[len(nums)-1]==13:
            nums[len(nums)-1]=0
        total=total+nums[i]
    print(nums)
    return total
print(sum13([1, 2, 2, 1, 13]))
"""


a=2
b=1
print(f"{a} and {b}")
c=a
a=b
b=c
print(f"{a} and {b}")