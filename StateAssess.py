st = "Print only the words that start with s in the sentence"
tr = st.split()
print(tr)
for a in tr:
    if 's' in a:
        if 's' in a[-1]:
            continue
        print(a)
even = list(range(0,10,2))
print(even)
"""myList = []
for t in range(1,50):
    if t%3 == 0:
        myList.append(t)
print(myList)"""
#into list comprehension
myList = [t for t in range(1,50) if t%3==0]
print(myList)

rt = "Print every word in this sentence that has an even number of letters"
secList = rt.split()
for r in secList:
    if len(r)%2==0:
        print(r)

print(list(range(1,101)))
for s in range(1,101):
    if s%3==0 and s%5==0:
            print(f"\nfizzBuzz:{s}")
    if s%3==0:
        print("fizz")
    elif s%5==0:
        print("\nbuzz")
yt = "Create a list of the first letters of every word in this string"
"""thirdList = []
for h in yt.split():
    if h[0] in yt.split():
        thirdList.append(h)
print(thirdList)"""
thirdList= [x[0] for x in yt.split()]
print(thirdList)
