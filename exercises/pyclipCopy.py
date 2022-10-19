import re
import pyclip

def extractor (listType,specList):
    print(listType.title()+" list :")
    for item in specList:
        print("- "+item)
    print("\n")

txt = pyclip.paste(text = True)
emailList= list(set(re.findall(r"\S+@\S+",txt)))
for i in emailList:
    txt = txt.replace(i, '')
urlList = list(set(re.findall(r"\S+\.[a-zA-z0-9]{2,5}\S*",txt)))
contactList = list(set(re.findall(r"\+|[0-9\s]+\d", txt)))

extractor("email",emailList)
extractor("contact",contactList)
extractor("url",urlList)