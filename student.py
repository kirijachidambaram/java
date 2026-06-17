students = []

while True:
    print("\n1.Add Student")
    print("2.View Students")
    print("3.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        dept = input("Enter department: ")

        students.append({
            "name": name,
            "dept": dept
        })

        print("Student Added Successfully")

    elif choice == "2":
        print("\nStudent List")

        for student in students:
            print(student["name"], "-", student["dept"])

    elif choice == "3":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")