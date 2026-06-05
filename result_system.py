students = {}

def add_student():
    print("\n--- Add Student ---")
    roll = input("Roll Number: ")
    if roll in students:
        print("Student already exists!")
        return
    name = input("Student Name: ")
    m1 = float(input("Marks - Subject 1 (out of 100): "))
    m2 = float(input("Marks - Subject 2 (out of 100): "))
    m3 = float(input("Marks - Subject 3 (out of 100): "))
    m4 = float(input("Marks - Subject 4 (out of 100): "))
    m5 = float(input("Marks - Subject 5 (out of 100): "))

    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    students[roll] = {
        "name": name,
        "marks": [m1, m2, m3, m4, m5],
        "total": total,
        "percentage": round(percentage, 2),
        "grade": grade
    }
    print(f"\nStudent '{name}' added successfully!")
    print(f"Total: {total} | Percentage: {percentage:.2f}% | Grade: {grade}")

def view_all():
    print("\n--- All Students ---")
    if not students:
        print("No students found!")
        return
    print(f"{'Roll':<10} {'Name':<20} {'Total':<8} {'Percentage':<12} {'Grade'}")
    print("-" * 55)
    for roll, data in students.items():
        print(f"{roll:<10} {data['name']:<20} {data['total']:<8} {data['percentage']:<12} {data['grade']}")

def search_student():
    print("\n--- Search Student ---")
    roll = input("Enter Roll Number: ")
    if roll in students:
        d = students[roll]
        print(f"\nRoll Number : {roll}")
        print(f"Name        : {d['name']}")
        print(f"Marks       : {d['marks']}")
        print(f"Total       : {d['total']}")
        print(f"Percentage  : {d['percentage']}%")
        print(f"Grade       : {d['grade']}")
    else:
        print("Student not found!")

def update_student():
    print("\n--- Update Student ---")
    roll = input("Enter Roll Number to update: ")
    if roll not in students:
        print("Student not found!")
        return
    print(f"Updating marks for: {students[roll]['name']}")
    m1 = float(input("New Marks - Subject 1 (out of 100): "))
    m2 = float(input("New Marks - Subject 2 (out of 100): "))
    m3 = float(input("New Marks - Subject 3 (out of 100): "))
    m4 = float(input("New Marks - Subject 4 (out of 100): "))
    m5 = float(input("New Marks - Subject 5 (out of 100): "))

    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    students[roll]["marks"] = [m1, m2, m3, m4, m5]
    students[roll]["total"] = total
    students[roll]["percentage"] = round(percentage, 2)
    students[roll]["grade"] = grade
    print(f"Updated! New Grade: {grade} | Percentage: {percentage:.2f}%")

def delete_student():
    print("\n--- Delete Student ---")
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        name = students[roll]["name"]
        del students[roll]
        print(f"Student '{name}' deleted successfully!")
    else:
        print("Student not found!")

def main():
    print("=" * 45)
    print("   STUDENT RESULT MANAGEMENT SYSTEM")
    print("=" * 45)

    while True:
        print("\n--- MENU ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student Marks")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("\nChoose option (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("\nThank you! Goodbye!")
            break
        else:
            print("Invalid option! Please choose 1-6.")

main()
