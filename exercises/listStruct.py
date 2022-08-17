#question1

list1 = [100, 200, 300, 400, 500]
for a in range(len(list1)-1,-1,-1):
    print(list1[a])
#or...
print(list1[::-1])

#question2
list3 = ["M", "na", "i", "Ke"]
list4 = ["y", "me", "s", "lly"]

list5=[]

for a in list3:
    for b in list4:
        if list3.index(a)==list4.index(b):
            list5.append(a+b)
print(list5)

#or.....................................
list5=[a+b for a in list3 for b in list4 if list3.index(a)==list4.index(b)]
print(list5)

#question3
numbers = [1, 2, 3, 4, 5, 6, 7]
numSquared = [a**2 for a in numbers]
print(numSquared)

#question4
list6 = ["Hello ", "take "]
list7 = ["Dear", "Sir"]
list8=[]
for a in list6:
    for b in list7:
        list8.append(a+b)
print(list8)

# or........
list8=[a+b for a in list6 for b in list7]
print(list8)

#question5

list9 = [10, 20, 30, 40]
list10 = [100, 200, 300, 400]

for a in range(len(list9)):
    print(list9[a], list10[3-a])

#question6
list11 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
list12=[a for a in list11 if a!=""]
print(list12)


#question7
list13 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list13[2][2].insert(2,7000)
print(list13)

#question8
list14 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]

list14[2][1][2].extend(sub_list)
print(list14)

#question9
list15 = [5, 10, 15, 20, 25, 50, 20]
list16=list15[::-1]
for a in list15:
    if list16.count(a)>1:
        list16.remove(a)
        t=list16.index(a)
        list16.remove(a)
        list16.insert(t, 200)
        list16.insert(0, 20)
print(list16[::-1])

#question10
list17 = [5, 20, 15, 20, 25, 50, 20]
list18=[a for a in list17 if list17.count(a)==1]
print(list18)
