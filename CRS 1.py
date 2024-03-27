class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
        self.students = []

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.registered_courses = []

def create_course(course_list, course_id, course_name):
    new_course = Course(course_id, course_name)
    course_list.append(new_course)
    print(f"Course '{course_name}' (ID: {course_id}) created successfully!")

def remove_course(course_list, course_id):
    for course in course_list:
        if course.course_id == course_id:
            course_list.remove(course)
            print(f"Course with ID {course_id} removed successfully.")
            break
    else:
        print(f"Course with ID {course_id} not found.")

def view_course_list(course_list):
    print("Course List:")
    for course in course_list:
        print(f"ID: {course.course_id}, Name: {course.course_name}")

def enroll_student(course_list, student_list, course_id, student_id):
    for course in course_list:
        if course.course_id == course_id:
            for student in student_list:
                if student.student_id == student_id:
                    course.students.append(student)
                    student.registered_courses.append(course)
                    print(f"Student {student.student_name} enrolled in course {course.course_name}.")
                    break
            else:
                print(f"Student with ID {student_id} not found.")
            break
    else:
        print(f"Course with ID {course_id} not found.")

def remove_student(course_list, student_list, student_id):
    for student in student_list:
        if student.student_id == student_id:
            for course in student.registered_courses:
                course.students.remove(student)
            student_list.remove(student)
            print(f"Student with ID {student_id} removed successfully.")
            break
    else:
        print(f"Student with ID {student_id} not found.")

def register_student(course_list, student_list, student_id, course_id):
    enroll_student(course_list, student_list, course_id, student_id)

def search_student_details(student_list, student_id):
    for student in student_list:
        if student.student_id == student_id:
            print(f"Student ID: {student.student_id}")
            print(f"Student Name: {student.student_name}")
            print("Registered Courses:")
            for course in student.registered_courses:
                print(f"- {course.course_name}")
            break
    else:
        print(f"Student with ID {student_id} not found.")

def list_students_for_course(course_list, course_id):
    for course in course_list:
        if course.course_id == course_id:
            print(f"Students registered for course {course.course_name}:")
            for student in course.students:
                print(f"- {student.student_name} (ID: {student.student_id})")
            break
    else:
        print(f"Course with ID {course_id} not found.")

def main():
    course_list = []
    student_list = []

    while True:
        print("\nCourse Registration System")
        print("1. Create a course")
        print("2. Remove a course")
        print("3. View course list")
        print("4. Enroll a student")
        print("5. Remove a student")
        print("6. Register a student for a course")
        print("7. Search student details by ID")
        print("8. List students registered for a course")
        print("9. EXIT")

        choice = input("Enter your choice: ")

        if choice == '1':
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            create_course(course_list, course_id, course_name)
        elif choice == '2':
            course_id = input("Enter course ID to remove: ")
            remove_course(course_list, course_id)
        elif choice == '3':
            view_course_list(course_list)
        elif choice == '4':
            student_id = input("Enter student ID: ")
            student_name = input("Enter student name: ")
            student_list.append(Student(student_id, student_name))
        elif choice == '5':
            student_id = input("Enter student ID to remove: ")
            remove_student(course_list, student_list, student_id)
        elif choice == '6':
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")
            register_student(course_list, student_list, student_id, course_id)
        elif choice == '7':
            student_id = input("Enter student ID: ")
            search_student_details(student_list, student_id)
        elif choice == '8':
            course_id = input("Enter course ID: ")
            list_students_for_course(course_list, course_id)
        elif choice == '9':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
