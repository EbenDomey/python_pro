tuple1 = (10, 20, 30, 40, 50)
tuple_list = list(tuple1)
tuple_list.reverse()
tuple_return = tuple(tuple_list)
print(tuple_return)


tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])

tuple2 = (10, 20, 30, 40)
(a, b, c, d) = tuple2
print(a, b, c, d)


tuple3 = (11, 22)
tuple4 = (99, 88)
tuple5 = tuple3
tuple3 = tuple4
tuple4 = tuple5
print("tuple3: ", tuple3)
print("tuple4: ", tuple4)


tuple6 = (11, 22, 33, 44, 55, 66)
tuple_list = []
for a in tuple6:
    if a == 44 or a == 55:
        tuple_list.append(a)
print(tuple(tuple_list))

tuple7 = (11, [22, 33], 44, 55)
tuple7[1][0] = 222
print(tuple7)

tuple8 = (("a", 23), ("b", 37), ("c", 11), ("d", 29), ("e", 1))
tuple8 = tuple(sorted(list(tuple8), key=lambda x: x[1]))
print(tuple8)

tuple9 = (50, 10, 60, 70, 50)
print(tuple9.count(50))

tuple10 = (4, 45, 45, 45)
a = tuple10[1]
print(tuple10.count(a) == len(tuple10))

# or.....

"""
result = ""
for a in range(len(tuple10)):
    if a + 1 <= len(tuple10) - 1:
        if result == False:
            result = False
        else:
            result = tuple10[a] == tuple10[a + 1]
    else:
        break

print(result)"""
