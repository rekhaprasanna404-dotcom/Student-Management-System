students = {}

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = float(input("Enter marks (out of 600): "))

        percentage = (marks / 600) * 100

        if percentage >= 90:
            grade = "A"
        elif percentage >= 75:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        else:
            grade = "D"

        students[name] = {
            "marks": marks,
            "percentage": percentage,
            "grade": grade
        }

        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records:")
            for name, details in students.items():
                print(f"\nName: {name}")
                print(f"Marks: {details['marks']}")
                print(f"Percentage: {details['percentage']:.2f}%")
                print(f"Grade: {details['grade']}")

    elif choice == "3":
        name = input("Enter student name to search: ")

        if name in students:
            details = students[name]
            print(f"\nName: {name}")
            print(f"Marks: {details['marks']}")
            print(f"Percentage: {details['percentage']:.2f}%")
            print(f"Grade: {details['grade']}")
        else:
            print("Student not found!")

    elif choice == "4":
        name = input("Enter student name to delete: ")

        if name in students:
            del students[name]
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")