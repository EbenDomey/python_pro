#finding volume of a sphere
def vol(rad):
    vol=(4/3)*3.14*rad**3
    return vol

print(vol(5))

#checking to see if a number is in a given range
def ran_check(num,low,high):
    return num in range(low,high)

print(ran_check(15,0,30))


#checking the total number of capital letters and smaller letters in a sentence
def up_low(str):
    count=0
    tab=0
    t=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
    h=[t[x].lower() for x in range(len(t))]
    for i in range(len(str)):
        u=str[i]
        if u in t:
            count=count+1
        elif u in h:
            tab=tab+1
    print("Upper case: ")
    print(count)
    print("Lower case: ")
    print(tab)

up_low("Hello Mr. Rogers, how are you this fine Tuesday?")


#creating a list of unique numbers
def unique_list(l):
    t=[]
    for i in range(len(l)):
        q=l[i]
        if q in l[i+1:]:
            continue
        else:
            t.append(q)
    for i in range(len(t)):
        print(t[i])

unique_list([1,2,4,3,3,5,7,1,5,3,9,2])

#multiplying a list of numbers
def multiply(numbers):
    product=1
    for i in range(len(numbers)):
        product*= numbers[i]
    return product

print(multiply([1,2,3,-4]))


#checking for palindrome string
def palindrome(str):
    str = str.replace(" ", "")
    return str==str[::-1]

print(palindrome("nurses run"))

def ispanagram(str):
    str = str.replace(" ", "")
    str = str.replace("-","")
    str = str.replace(",","")
    t=''
    for i in range(len(str)):
        q=str[i]
        if q in str[i+1:]:
            continue
        else:
            t=t+q

    return len(t)==26

print(ispanagram("i am eben and my queued cute and favorite anime is dragonball z joke play with the nine-tails fox"))

# homework done!!!!