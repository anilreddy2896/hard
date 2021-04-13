## ziping
from zipfile import *
f=ZipFile("file1.zip","w",ZIP_DEFLATED)
f.write("names.txt")