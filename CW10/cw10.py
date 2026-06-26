# Required Structures
users = {
    'jperez':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Juan Pérez'
    },
    'dromo':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Daniela Romo'
    },
    'mjuarez':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Mauricio Juárez'
    },
    'mlopez':	{
        'password': '1234',
        'rol': 'student',
        'name': 'María López'
    },
    'euc':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Ernesto Uc'
    },
    'cbalam':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Carlos Balam'
    },
    'jpedrozo':	{
        'password': '1234',
        'rol': 'professor',
        'name': 'Jorge Pedrozo'
    },
    'dgamboa':	{
        'password': '1234',
        'rol': 'coordinator',
        'name': 'Didier Gamboa'
    }
}
 
subjects = (
    "Discrete Mathematics",
    "Programming",
    "English II",
    "Differential Calculus",
    "Probability and Statistics",
    "Computer and Server Architecture",
    "Socio-Emotional Skills and Conflict Management"
)
 
notes = {
    'jperez': {
        'Discrete Mathematics': 8.5,
        'Programming': 9.2,
        'English II': 9.0,
        'Differential Calculus': 7.8,
        'Probability and Statistics': 8.3,
        'Computer and Server Architecture': 6.8,
        'Socio-Emotional Skills and Conflict Management': 9.5
    },
    'dromo': {
        'Discrete Mathematics': 9.0,
        'Programming': 6.7,
        'English II': 9.4,
        'Differential Calculus': 6.2,
        'Probability and Statistics': 9.1,
        'Computer and Server Architecture': 6.5,
        'Socio-Emotional Skills and Conflict Management': 9.8
    },
    'mjuarez': {
        'Discrete Mathematics': 7.5,
        'Programming': 8.0,
        'English II': 8.5,
        'Differential Calculus': 7.0,
        'Probability and Statistics': 7.8,
        'Computer and Server Architecture': 6.2,
        'Socio-Emotional Skills and Conflict Management': 8.9
    },
    'mlopez': {
        'Discrete Mathematics': 9.5,
        'Programming': 9.8,
        'English II': 9.2,
        'Differential Calculus': 9.0,
        'Probability and Statistics': 9.6,
        'Computer and Server Architecture': 9.4,
        'Socio-Emotional Skills and Conflict Management': 10.0
    },
    'euc': {
        'Discrete Mathematics': 8.2,
        'Programming': 6.9,
        'English II': 8.8,
        'Differential Calculus': 6.0,
        'Probability and Statistics': 6.4,
        'Computer and Server Architecture': 8.1,
        'Socio-Emotional Skills and Conflict Management': 9.0
    },
    'cbalam': {
        'Discrete Mathematics': 8.8,
        'Programming': 9.0,
        'English II': 8.5,
        'Differential Calculus': 6.6,
        'Probability and Statistics': 8.9,
        'Computer and Server Architecture': 8.7,
        'Socio-Emotional Skills and Conflict Management': 9.2
    }
}

while True:
    person = input("User: ")
    if person in users:
        user = users[person]
        while True:
            input_password = input("Password: ")
            if input_password == user["password"]:
                break
            else:
                print("Wrong user password")
        print(f"Bienvenid@! {user["name"]} ({user["rol"]})")


        if user["rol"] == "student":
            print(f"{'*' * 30}\nSchool Report\n{"*" * 30}")
            user_subjects = notes[person]
            approved_subjects = []
            failed_subjects = []
            for subject, grade in user_subjects.items():
                if grade >= 7:
                    print(f"{subject:50.50} : {grade}")
                    approved_subjects.append(subject)
                else:
                    failed_subjects.append(subject)
            print("\n")
            print(f"Aproved: {approved_subjects}")
            print(f"Pending: {failed_subjects}") 


        elif user["rol"] == "professor":
            print(f"{'*' * 30}\nStudents\n{"*" * 30}")

            for student_user in users:
                student_info = users[student_user]
                if student_info["rol"] == "student":
                    student_name = student_info["name"]
                    print(f"User: {student_user:30.30}|  Student:{student_name}")
            print("\n")

            while True:
                finish = input("Type 'end' to exit, something else to continue:")
                if finish == "end":
                    break
                else:
                    pass
                while True:
                    student = input("Student to grade (username): ")
                    if student in users and users[student]["rol"] == "student":
                        break
                    else:
                        print("Invalid user, try again")
                print(f"{'*' * 30}\nSubjects\n{"*" * 30}")
                for subject in subjects:
                    print(subject)
                print("\n")

                subject_to_grade = input("Subject to grade: ")
                if subject_to_grade in subjects:
                    new_grade = int(input("New grade: "))
                    print("\n")
                    old_grade = notes[student][subject_to_grade]
                    confirmation = input(f"Do you confirm (yes/no)?\n{subject_to_grade}: {old_grade} ==> {new_grade}\n")
                    if confirmation == "yes":
                        notes[student][subject_to_grade] = new_grade
                        print("\n")
                        print(f"Grade updated!\n{notes[student]}")


        elif user["rol"] == "coordinator":

            print(f"{'*' * 30}\nProfessor\n{"*" * 30}")
            for professor in users:
                professor_info = users[professor]
                if professor_info["rol"] == "professor":
                    professor_name = professor_info["name"]
                    print(f"User: {professor:30.30}|  Professor:{professor_name}")
            print("\n")

            print(f"{'*' * 30}\nStudents\n{"*" * 30}")
            for student_user in users:
                student_info = users[student_user]
                if student_info["rol"] == "student":
                    student_name = student_info["name"]
                    print(f"User: {student_user:30.30}|  Student:{student_name}")
            print("\n")

            print(f"{'*' * 30}\nStudents\n{"*" * 30}")
            subject_word = "SUBJECTS"
            print(f"{subject_word:10.10}|", end="")
            for student in users.keys():
                if users[student]["rol"] == "student":
                    print(f"{student:10.10}|", end="")
            print("")
            print("-" * 100)

            for subject1 in subjects:
                print(f"{subject1:10.10}|", end="")
                for student in notes:
                    grade = notes[student][subject1]
                    print(f"{grade:10.10}|", end="")
                print("")
        exit =  input("Type 'end' to exit: ")
        if exit == "end":
            break
    else:
        print("Invalid user")