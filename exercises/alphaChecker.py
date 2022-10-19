txt = "Peter Piper ate a pair of pickled pepper".lower()
txt = txt.replace(" ", "")
txtLen = len(txt)
myDict = {}
count = 0
# for t in txt:
#     y = txt.count(t)
#     myDict[t] = y

for i in range(txtLen):
    for t in txt:
        if txt[i] == t:
            count += 1
            myDict[t] = count
    count = 0
print(myDict)