
students = []

# Function to load students from a text file
def load_students():
    global students
    try:
        with open('students.txt', 'r') as file:
            students = []
            for line in file:
                line = line.strip()
                if line:  # Only process non-empty lines
                    if ' - ' in line:
                        name, grade = line.split(' - ')
                        students.append({"name": name, "grade": grade})
    except FileNotFoundError:
        students = []

# Function to save students to a text file
def save_students():
    with open('students.txt', 'w') as file:
        for student in students:
            file.write(f"{student['name']} - {student['grade']}\n")

# Function to add a student
def student_grade(name, grade):
    students.append({"name": name, "grade": grade})
    save_students()

# Function to view students
def view_students():
    if not students:
        print("No students yet.")
    else:
        for index, student in enumerate(students, start=1):
            print(f"{index}. Name: {student['name']}, Grade: {student['grade']}")

# Function to update a student's grade
def update_grade(index, new_grade):
    if 0 <= index < len(students):
        students[index]['grade'] = new_grade
        save_students()
        print("Grade updated!")
    else:
        print("Invalid student number.")

# Function to delete a student
def delete_student(index):
    if 0 <= index < len(students):
        students.pop(index)
        save_students()
        print("Student deleted!\n")
    else:
        print("Invalid student number.\n")

# Load students when the program starts
load_students()

# Main program loop
while True:
    print('\nMENU\n\n1. Add student and grade\n2. View students\n3. Update student grade\n4. Delete student\n5. Exit')
    choice = input('\nEnter choice: ')
    
    if choice == '1':
        name = input('\nEnter student name: ')
        grade = input('Enter student grade: ')
        student_grade(name, grade)
        
    elif choice == '2':
        print('\n')
        view_students()
        
    elif choice == '3':
        print('\n')
        view_students()
        student_number = int(input('\nEnter the student number to update: '))
        new_grade = input('Enter new grade: ')
        update_grade(student_number - 1, new_grade)
        
    elif choice == '4':
        print('\n')
        view_students()
        student_number = int(input('\nEnter the student number to delete: '))
        delete_student(student_number - 1)
                             
    elif choice == '5':
        print('Goodbye!')
        break
    else:
        print('Invalid choice. Try again!')

        
