students = {
    "muzan":[80,50], # if in {}, it is called a set, if in [] it is called a list
    "daniel":[50],
    "wan": [70],
}

def check_list():
    if not students:
        print("No students data in the list yet.")
        return False
    return True

def addstudent(name):
    if name not in students:
        students[name] = []
        print(f"Student {name} added successfully.")
        
def addgrade(name, grade):
    if name not in students:
        print(f"{name} is not in the student list yet. Please add first.")
    else:
        students[name].append(grade)
        print(f"Grade {grade} added for {name}.")


def display_all_students():
    if check_list():
        for name, grades in students.items():
            avg = average_grade(name)
            print(f"Name: {name} | Grades: {grades} | Average Grade: {avg}")
    else:
        print("Enter Student data first")

def average_grade(name):
    if len(students[name]) == 0:
        print(f"{name} has no grade yet.")
        return 0
    total = sum(students[name])
    avg = round(total / len(students[name]),2)
    return avg

def highest_scorer():
    highest_name = ""
    highest_grade=float('-inf')
    if check_list():
        for name, grades in students.items():
            avg = average_grade(name)
            if avg > highest_grade:
                highest_name = name
                highest_grade = avg
        print(f"The highest scorer is {highest_name} with an average grade of {highest_grade}")
    else:
        print("Enter Student data first")

def lowest_scorer():
    lowest_name = ""
    lowest_grade=float('inf')
    if check_list():
        for name, grades in students.items():
            avg = average_grade(name)
            if avg < lowest_grade:
                    lowest_grade = avg
                    lowest_name = name
        print(f"The lowest scorer is {lowest_name} with an average grade of {lowest_grade}")
    else:
        print("Enter Student data first")
    
continue_session = True

print("Welcome to the student grade tracker")

while continue_session:
    print("Please select an option:")
    print("1. Add New Student")
    print("2. Add Grade for Existing Student")
    print("3. View All Students and their Grades")
    print("4. Find the highest scorer")
    print("5. Find the lowest scorer")
    print("6. Exit")

    choice =input("Choose an option (1-6):")

    if choice =="1":
        name = input("Enter the student's name: ")
        addstudent(name)
    elif choice == "2":
        name = input("Enter the name of the student you want to add a grade for: ")
        try:
            grade = int(input("Enter the grade: "))
            addgrade(name, grade)
        except ValueError:
            print("Invalid input. Please enter a valid grade.")
    elif choice == "3":
        display_all_students()
    elif choice == "4":
        highest_scorer()
    elif choice == "5":
        lowest_scorer()
    else:
        continue_session = False
        print("Exiting the program. Goodbye!")
