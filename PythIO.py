#this is for the other modes which are found in the open function
#syntactically open(fileName, mode,)
"""
    the modes are four namely:
    r = means read only
    w = means write only it also overwrites whatever file it is assigned to
    a = means append you add extra lines to the file
    w+ = means write and read this allows you to perform multiple in one and still overwrites existing file
    r+ = means read and write in that order also overwrites the file
"""
#for read
with open("pyIO3.txt", mode= 'r') as f:
    inner = f.read()
    print(inner)
#for append
with open("pyIO3.txt", mode= 'a') as fr:
    inter = fr.write("\nEminem is awesome")
#to read appended file
with open("pyIO3.txt", mode='r') as fr:
    glance = fr.read()
    print(glance)


# for write
with open("PythIO.txt", mode= 'w') as ft:
    assign = ft.write("I got bags in the coup touch me I'll shoot")
#to read
with open("PythIO.txt", mode='r') as ft:
    cont = ft.read()
    print(cont)
