import re
nums = [1,2,3,4,5]

#alternative one for question 3
for i in range(10):
    num = int(input(f"Number {i+1}: "))
    nums.append(num)
# nums.sort()
# a= nums[-1]
# b= nums[-2]
# print("the maximum and minimum numbers respectively are", a, b)

#alternative two for question 3
newList = []
for i in range(len(nums)):
    a = 0
    for num in nums:
        if num > a:
            a = num
    newList.append(a)
    index = nums.index(a)
    nums.pop(index)
# print(newList)
print(f"the maximum number is {newList[0]} and second largest number is {newList[1]}")







# facRec = int(input("Enter a number to know its factorial: "))
# fact = 1
# for i in range(facRec,1,-1):
#     fact *= i
# print(fact)

# nums = [1,2,3,4,5,4,7,8,9,5,1,3,6,4,2,8,9,7,1,3]
# numDict = {}
# count = 0
# for i in range(20):
#     for num in nums:
#         if num == i:
#             count +=1
#             numDict[i] = count
#     count = 0
# print(numDict)

txt = "Hello, I'm Jappy-Lappy-Happy".lower()
txt = re.sub("[-,'\s]", "", txt)
# txt = txt.replace(r"[-,'!]", "")
# txt = txt.replace(",", "",)
# txt = txt.replace("'", "",)
# txt = txt.replace(" ", "",)
print(txt[::-1])