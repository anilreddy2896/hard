##### csv
import csv
with open("student.csv","w",newline='') as f :
    w=csv.writer(f)
    w.writerow(["sname","rollnumber"])
    n=int(input("enter number of students: "))
    for i in range(n):
        sname=input("Enter student name: ")
        rollnumber=int(input("enter the rollnumber: "))
        w.writerow([sname,rollnumber])
print("done everything printed in csv file")