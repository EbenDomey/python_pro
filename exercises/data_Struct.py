
#question1
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
odd_list=[a for a in l1 if l1.index(a)%2!=0]
even_list= [a for a in l1 if l1.index(a)%2==0]
print(odd_list)
print(even_list)
print(odd_list+even_list)


#question2
list2=[34, 54, 67, 89, 11, 43, 94]
a = list2.pop(4)

list2.insert(2,a)
list2.pop()


#question3
sample_list3 = [11, 45, 8, 23, 14, 12, 78, 45, 89]
first_slice = sample_list3[:3]
second_slice = sample_list3[3:6]
third_slice= sample_list3[6:]


print(first_slice[::-1])
print(second_slice[::-1])
print(third_slice[::-1])


#question4
sl4 = [11, 45, 8, 11, 23, 45, 23, 45]
d = dict()
for a in sl4:
    if a in d:
        d[a] += 1
    else:
        d[a] = 1
print(d)

#question5
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

my_values =[]
for a in first_list:
    for b in second_list:
        if first_list.index(a) == second_list.index(b):
            my_values+=[(a,b)]
            s= set(my_values)

print(s)

#question6

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
set_cast = list(first_set)
sec_set_cast = list(second_set)

for a in set_cast:
    for b in sec_set_cast:
        if a == b:
            set_cast.remove(a)

res_set = set(set_cast)
print(res_set)

#question7
first_sets = {27, 43, 34}
second_sets = {34, 93, 22, 27, 43, 53, 48}

test1= first_sets.issubset(second_sets)
test2= second_sets.issubset(first_sets)
print(f"Is first_set a subset of second_set? {test1}")
print(f"Is second_set a subset of first_set? {test2}")

test3=first_sets.issuperset(second_sets)
test4= second_sets.issuperset(first_sets)
print(f"\nIs first_set a superset of second_set? {test3}")
print(f"Is second_set a superset of first_set? {test4}")

if test1 and not test3:
    first_sets.clear()
elif test2 and not test4:
    second_sets.clear()
else:
    print("No clear")

print(f"First set: {first_sets}")
print(f"Second set: {second_sets}")


#question8
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'John':47, 'Emma':69, 'Kelly':76, 'Jason':97}

for a in roll_number:
    if a not in sample_dict.values():
        roll_number.remove(a)
roll_number.remove(95)
print(roll_number)


#question9
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
speed_list=[]
for a in speed.values():
    if a not in speed_list:
        speed_list.append(a)
    else:
        continue
print(speed_list)

#question10
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
final_list =[]

for y in sample_list:
    if y not in final_list:
        final_list.append(y)
    else:
        continue
print(f"Tuple transformation: {tuple(final_list)}")
print(f"Maximum value: {max(final_list)}")
print(f"Minimum value: {min(final_list)}")