import json #keys should be string
student = {
    "name" : "khwla",
    "age" : "18",
    "rollno" : "73",
}

with open("student.json","w") as f:
    json.dump(student,f)

with open("student.json", "r") as f:
    print(json.load(f))    
