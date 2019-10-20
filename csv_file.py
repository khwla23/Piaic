import csv
with open(" student.csv", "a", newline="") as f:
    data_handler=csv.writer(f, delimiter = ",") 
    name = input(" enter name of the student: ")
    age = input(" enter age of the student :")
    rollno= input(" enter Roll number of the student :")
    data_handler.writerow([name,age,rollno])