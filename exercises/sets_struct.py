# question1

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
sample_set.update(sample_list)
print(sample_set)


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1.intersection(set2)
print(set3)

set4 = {10, 20, 30, 40, 50}
set5 = {30, 40, 50, 60, 70}
set6 = set4.union(set5)
print(set6)

set7 = {10, 20, 30}
set8 = {20, 40, 50}
set9 = set7.difference(set8)
print(set9)

set10 = {10, 20, 30, 40, 50}
for i in range(10, 40, 10):
    set10.discard(i)
print(set10)

set11 = {10, 20, 30, 40, 50}
set12 = {30, 40, 50, 60, 70}
set_union = set11.union(set12)
set_intersection = set11.intersection(set12)
for a in set_intersection:
    set_union.discard(a)
print(set_union)


set13 = {10, 20, 30, 40, 50}
set14 = {60, 70, 80, 90, 10}
print(set13.intersection(set14))

set14 = {10, 20, 30, 40, 50}
set15 = {30, 40, 50, 60, 70}

set_union2 = set14.union(set15)
set_intersection2 = set14.intersection(set15)
print(set_union2.difference(set_intersection2))

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

for b in set1.difference(set2):
    set1.discard(b)
print(set1)
