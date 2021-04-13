#### to know present working directory

import os
import time
## to know present working directory 
cwd=os.getcwd()
print("present working directory",cwd)

# creating a directory
print("folders is creating")
#os.mkdir("Folders")
time.sleep(10)


### creating the directory inside the existing directory
os.mkdir("Folders/heros")
print("folders/heros is creating")

time.sleep(10)

## creating the directories without existing of the directories
os.makedirs("sub1/sub2/sub3")
time.sleep(10)
# to remove all particular directory
os.rmdir("Folders/heros")

# to remove all directorie
os.removedirs("sub1/sub2/sub3")

#rename
os.rename("Folders","newfolder")