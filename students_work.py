students = {}

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        mark = int(input("Enter Student Mark: "))
        students[name] = mark
        print("Student Added Successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No Students Found!")
        else:
            print("\nStudent Records")
            print("----------------")
            for name, mark in students.items():
                print(f"Name: {name} | Mark: {mark}")

    elif choice == "3":
        search = input("Enter Student Name to Search: ")
        if search in students:
            print(f"{search}'s Mark: {students[search]}")
        else:
            print("Student Not Found!")

    elif choice == "4":
        delete = input("Enter Student Name to Delete: ")
        if delete in students:
            del students[delete]
            print("Student Deleted Successfully!")
        else:
            print("Student Not Found!")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Please Try Again.")