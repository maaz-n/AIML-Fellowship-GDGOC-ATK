students = []

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")
    
    student = {
        'name': name,
        'age': age,
        'grade': grade
    }
    
    students.append(student)
    print(f"Added {name} to records.")

def display_students():
    if not students:
        print("No students in records.")
    else:
        print("Student Records:")
        for i, student in enumerate(students, 1):
            print(f"{i}. {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

def update_student():
    try:
        index = int(input("Enter student number to update: ")) - 1
        if 0 <= index < len(students):
            print(f"Updating {students[index]['name']}")
            students[index]['age'] = int(input("New age: "))
            students[index]['grade'] = input("New grade: ")
            print("Student updated!")
        else:
            print("Invalid student number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    print("\n1. Add student")
    print("2. View student")
    print("3. Update student")
    print("4. Exit")
    choice = input("Choose: ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        update_student()
    elif choice == '4':
        print("Goodbye!")
        break