f = open("demo.txt", "r")#read file
print(f.read())
c=open("demosfile.txt","r")
print(c.read())
w= open("demo.txt", "a") #update file with additional data
w.write("Now the file has one more line!")
ow = open("demo.txt", "w") #delete entire content and add new content
ow.write("Woops! I have deleted the content!")
new= open("demosfile.txt","w") #create new file and add content
new.write("a new file is created with python program and content is added")
