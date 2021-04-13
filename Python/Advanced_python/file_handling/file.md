

282152706596
To store the program information for future use and permanetly
to store very less amount of data we use the files 

## Types of files:
   1. Text files:
      ex: text 
   2. binary file:
       ex: images,videos

## opening a file:

when u r trying to open a file we need to specify the purpose of opening the file ,like read,write,append

To do this we use the python inbuilt function Open(filename,mode)

## allowed modes :

1. r : this is default mode (read)
2. w(write): override if the file exist ,if not exist it create
3. a(append):append the data if the file exists or else it creates
4. r+ (read and write)
5. w+(write and read): override and read
6. a+(append and read): willnot override
7. x: to open a file in exclusive creation mode for write operation (it will not override if the file exists ,it will throws an error if file exist)

This are for text files

For binary files:
rb,wb,ab,r+b,w+b,a+b,xb

After opening of every file the file should be closed .other resources will be wasted >>>>>> to close 
### f.close()

## varoius properties of file:
f.name
f.mode
f.closed
f.readable()
f.writable()

## writing the data to the text files

f.write(str)
f.writelines(listoflines)

## reading the file:
      1. character data:
          1.1 read(): to read complete data from file
          1.2 read(n): to read n characters
          1.3 readline(): to read only one line
          1.4 readlines():to read all lines into list

### with statement:
   if we use with statement we don't need to close the file explicitly it automatically closes even if exceptions occurs

   # tell():
       will tell current position of the cursor
## seek():
  to move the cursor to the particular position
//// in python2:
  f.seek(offset,fromwhere)
0 :from begining from the file(default)
1 :from current position
2 :from end of the file

for python 3 only 0 is allowed


## to check wheather a file is available or not

in the os module there is a sub module called path which helps to find the file 
os.path.isfile(<filename>)


## binary data handling:

## handling csv file
    import csv module in order to perform  csv related operations

## zip and unzip

 import zipfile 
 and create ZipFile class with default values filename.zip , mode, ZIP_DEFALTED--> this means the constant that represent zip file is created

 ZIP_STORED is a the constant that represent to unzip the file