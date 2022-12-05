import math



#exercise1

# list1 = ["Npepl1", "Rab13", "Reg4", "Asb17", "Clcnka", "Nup62", "Upf3a", "Kcnn1", "Ccdc151", "Arg1", "Tmem98", "Mtx3", "Isl1", "cat32", "Fam53c" ]
# list2 = ["Kcnj2", "Rab13", "Reg4","Nol6", "Masp2", "Clcnka", "Upf3a", "Kcnn1", "Arg1", "Krt75", "Smpd3", "Mtx3", "Trim8", "Fam53c", "cat32"]
# list3 = []

# for item in list1:
#     for ref in list2:
#         if item == ref:
#             list3.append(item)

# list3.sort()


# for item in range(len(list3)):
#     print(f"{item+1}. {list3[item]}")





#exercise 2

# for angles in range(1801):
#     sinTrans = math.sin(angles)
#     if math.fabs(sinTrans) < 0.01:
#         print(angles)

# variants = ["E23A", "P12S", "W88Y", "R32N"]
# unknownVariants = []
# count = 0

# while True:
#     varTest = input('Enter Variants: ')
#     if varTest.upper() in variants:
#         count += 1
#     elif len(varTest) == 0:
#         break
#     else:
#         print('Unknown Variant')
#         unknownVariants.append(varTest)

# print(f"\n\n\nKnown variants count: {count}")
# print(f"Unknown variants count: {len(unknownVariants)}")
# print(f"Unknown variants: {unknownVariants}")

# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]
# l3 = []
# l4 = []
# l5 = []

# for i in range(len(l1)):
#     if i % 2 != 0:
#         # print(l1[i])
#         l3.append(l1[i])

# # print("\n\n\n\n")
# for n in range(len(l2)):
#     if n % 2 == 0:
#         # print(l2[n])
#         l4.append(l2[n])

# l5 = l3 + l4
# print(l5)


# list1 = [54, 44, 27, 79, 91, 41]
# print(list1)
# removedItem = list1.pop(4)
# print("After: ",list1)

# list1.insert(2,removedItem)
# print(list1)
# list1.append(removedItem)
# print("Final command: ",list1)



sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89,5,4,3]
chunk = []
i = 1
step = round(len(sample_list) / 3)
for end in range(0,len(sample_list),step):
    chunk = sample_list[end: end + step]
    print(f"Chunk{i}: ",chunk)
    i += 1

