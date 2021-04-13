## writing the information to the text file
f=open("testfile.txt","w")
f.write("created by :")
list=['anil reddy\n']
f.writelines(list)
f.close() ## this is best programming language practise
