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