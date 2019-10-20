students = []
while True:
    print (" Press 1 to add student")
    print (" press 2 to search student")
    print (" press 3 to delete students")
    print ("press 4 to check number of students enrolled")
    print ( " press 5 to exit")
choice  =int(input(" Enter your choice"))
if choice == 1:
    student = {}
    student [ "Name"] = input (" please enter student name:")          
    student [ "Father name"] = input (" please Enter father name;")  
    student [ "Cell number"] = input (" please Enter cell number:")  
    students.append(students)
elif choice == 2:
    name = input(" Enter the name you want to search for:")
    for student in students:
       if student["Name"].lower() == name.lower() :
        print("Student with name "  + name + "found and details are avaliable")
        print (student)
elif choice == 3:        
    del student[ " Father name"]
    print (student) 
elif choice == 4:
    print (" we curently have " + str(len(students)) + 'Students')
elif choice == 5:
    break


