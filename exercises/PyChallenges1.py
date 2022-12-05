import re
# nums = [1,2,3,4,5]

weightsInPounds = 50
heightsInInches = 5

BMI = (weightsInPounds * 703) / (heightsInInches ** 2)
print(BMI)
if BMI < 18.5:
    print("Underweight")
elif BMI > 18.5 and BMI < 24.9:
    print("Overweight")
elif BMI > 25 and BMI < 29.9:
    print("Overweight")
else:
    print("Obese")

#question 2
items_dict = {'a': 239.99, 'b': 129.75, 'c': 99.95, 'd': 350.89}

item= input('Kind of items sold: ')
quantity = int(input('Number of items sold: '))

quantityCost = items_dict[item] * quantity
payPerWeek = 200 + (9/100*quantityCost)

print(f"Your pay for this week is: ${payPerWeek}")

#question 3
x=input("Enter numbers : ")
b = x.split(',')
nums = [int(a) for a in b]
#alternative one for question 3
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
print(newList)
# print(f"the maximum number is {newList[0]} and second largest number is {newList[1]}")

def find_factorial(t):
    factorial = 1
    for i in range(t,1,-1):
        factorial = factorial * i
    return factorial

t= int(input('Number: '))
# print(find_factorial(t))

#question 5
nums = [1,2,3,4,5,4,7,8,9,5,1,3,6,4,2,8,9,7,1,3]
numDict = {}
count = 0
# for i in range(20):
#     for num in nums:
#         if num == i:
#             count +=1
#             numDict[i] = count
#     count = 0
for num in nums:
    count = nums.count(num)
    numDict[num] = count
print(numDict)

#question 7
txt = "Hello, I'm Jappy-Lappy-Happy".lower()
# txt = re.sub("[-,'\s]", "", txt)
txt = txt.replace("-", "")
txt = txt.replace(",", "",)
txt = txt.replace("'", "",)
txt = txt.replace(" ", "",)
# print(txt[::-1])



