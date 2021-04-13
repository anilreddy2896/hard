string=input("Enter the string which you like : ")
l=string.split(' ')
word=input('enter the word which you want to search: ')
count=0
for i in l:
    if i == word:
        count+=1
print(count)
        