#number 1
#st='Print only the words that start with s in this sentence'
#mylist=st.split()
#for x in mylist:
#    if 's' in x[0]:
#        print(x)


# number 2
#for a in range(0,10,2):
#   print(a)


#number 3
#seclist= [a for a in range(1,50) if a%3==0 ]
#print(seclist)


#number 4
"""sy='Print every word in this sentence that has an even number of letters'
mylist=sy.split()
for x in mylist:
    if len(x)%2==0:
        print('even')
    else:
        print(x)
        """


"""for t in range(1,101):
    if t%3==0 and t%5==0:
        print('fizzBuzz')
    elif t%3==0:
        print('fizz')
    elif t%5==0:
        print('buzz')
    else:
        print(t)
        """


#number 5
"""sr='Create a list of the first letters of every word in this sentence'
list1=sr.split()
list2= [x[0] for x in list1]
print(list2)"""

"""t='ebenezer'
print(t[-2:])
result=""
for i in range(len(t)+1):
    result=result+ t[:i]
print(result)"""
#n=list(range(0,len(t)))
#print(n)
#print(t[:2]+t[2+1:])
"""if len(t)>1:
    h=t[1:len(t)-1]
    new=t[-1]+h+t[0]
    print(new)
else:
    print(t)"""

nums=[1, 2, 9,9,9,9]
list2=[]
list2.append(nums[1:])

print(list2)
"""count=0
for i in range(len(nums)):
    chec=nums[i]
    if chec==9:
      count = count +1
print(count)

nums=[1, 2, 9, 3, 4]
if len(nums)==0:
    print(False)
for i in range(4):
    check=nums[i]
    if check == 9:
      print(True)
    else:
      print(False)

def string_match(a,b):
    count=0
    for i in range(len(a)) and range(len(b)):
        set1=a[i:i+2]
        print("set1: "+set1)
        set2=b[i:i+2]
        print("set2: "+set2)
        if len(set1) and len(set2)!=2:
            continue
        elif set1==set2:
            count=count+1
    return count
print(string_match('abc', 'axc') )

def make_tags(tag, word):
  return "<"+tag+">"+word+"</"+tag+">"
print(make_tags('i', 'Yay'))

def make_out_word(out, word):
  return out[:2]+word+out[2:]
print(make_out_word('{{}}', 'Yay'))

def extra_end(str):
    if len(str)>=2:
        return str[-2:]*3
    else:
        return str
print(extra_end('hihihe'))

def rotate_left3(nums):
    if len(nums)==3:
        list3=[]
        list3.append(nums[1])
        list3.append(nums[2])
        list3.append(nums[0])
        return list3
    else:
        return nums
print(rotate_left3([7, 0, 0]))
print(range(10,0,-1))"""

def max_end3(nums):
    if nums[-1]>nums[0]:
        t=nums[-1]
        for i in range(len(nums)):
            nums[i]=t
        return nums
    elif nums[0]>nums[-1]:
        t=nums[0]
        for j in range(len(nums)):
            nums[j]=t
        return nums

print(max_end3([11, 5, 9]))