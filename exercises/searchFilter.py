import re
import pyclip
txt = "hello google.com i have paired up with w3schools.com and i have left https://www.programiz.com/python-programming/methods/list/index. My phone number is 0551426556. Other number are 0277063298 jO@yahoo.com ebenezerdomey@gmail.com"
txtList = re.split("\s", txt)
t = "com"
h = '@'
emailList = []
contactList = []
urlList = []
for x in txtList:
    u = re.search(r"^0", x)
    if h in x:
        emailList.append(x)
    if u:
        contactList.append(x)
    if t in x:
        if(x in emailList):
            continue
        urlList.append(x)
myDict = {'email': emailList, 'contact': contactList, 'URL': urlList}
print(myDict)