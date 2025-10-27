import csv

def add_student():
    name = input("Enter name: ")
    skills = input("Enter skills: ")
    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, skills])
        print("Student added successfully!")

def view_student():
    try:
        with open("students.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print("Name:", row[0])
                print("Skills:", row[1])
    except FileNotFoundError:
        print("Student data not found yet.")

while True:
    print("1. Add Student\n2. View Students\n3. Exit")
    choice = input("Choose option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_student()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Try again.")
