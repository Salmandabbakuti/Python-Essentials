import os
os.rmdir("myfolder")
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
  print("file deleted.")
else:
  print("The file does not exist")
 
