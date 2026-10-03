print("== Welcome to Student JSON Converter ==")




import json


while True:

    student_name = input("Please enter the student name : ")

    student_age = int(input("Please enter the student age : "))

    student_department = input("Please enter the student department : ")


    student = {
        "name": student_name,
        "age": student_age,
        "department": student_department
    }


    student_json = json.dumps(student)


    print(student_json)


    choice = input("Please enter c to continue or press any button to exit : ")

    if choice == "c":
        continue

    else:
        break




print("== Thank you so much for using my program ==")