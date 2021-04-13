
import csv
f1=open("student.csv",'r')
data=csv.reader(f1)
for i in data:
    for j in i:
        print(j,"\t",end='')
    print()
    

  