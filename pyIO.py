#today we gonna talk about accessing and manipulating files in python
#we first start with creating our file(Which is already done) in the same directory as the python file
#then we call upon it using the open function
myFiles = open('pyIO.txt')
#after opening we can begin to read it with the read method
print(myFiles.read())
#at this point the file should appear in the command line and also the cursor should have reached the end of the text so if read again..
print(myFiles.read())#an empty space will appear
#to fix that we have to place the cursor at the starting point by telling it to seek 0 using the seek method
myFiles.seek(0)
print(myFiles.read())
#sometimes too we want it placed in an iterable so we can play around with that we can do so by using the readlines method
myFiles.seek(0)
print(myFiles.readlines())
#this is what i know now but ill be back with more soon
#back again with more info
# now currently the file is still running so assuming you want to delete it an error would always pop up
#so if you wanna avoid that then close it with the close method
myFiles.close()
#or... if you wanna avoid this entire situation then u just have to use the with and as function which creates a code block
with open('pyIo.txt') as myFile:
    content = myFile.read()
    print(content)
#once that block is done executing the file will close automatically
#accessing remote files
# python has come up with a way in which you can access remote files by naming the entire directory from its root
#the syntax of this is that the escape character \ should be used twice so python has no issue 
with open("C:\\Users\\DomeyBenjamin\\Desktop\\pyIO2.txt") as secFile:
    info = secFile.read()
    print(info)