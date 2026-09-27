class Student:
    def __init__(self, name, student_id, email, age, department, *marks):
        self.name = name
        self.student_id = student_id
        self.__email = email       # Encapsulation
        self.age = age
        self.department = department
        self.__marks = list(marks) # Encapsulation

    # Getter for private email
    def get_email(self):
        return self.__email

    # Setter for private email
    def set_email(self, email):
        self.__email = email

    # Method Overloading using *args
    def add_marks(self, *marks):
        """
        Allows adding one or multiple marks.
        Example:
            student.add_marks(80)
            student.add_marks(75, 85, 90)
        """
        self.__marks.extend(marks)

    def display_info(self):
        print("\n--- Student Information ---")
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Email: {self.__email}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print(f"Marks: {self.__marks}")

    def calculate_result(self):
        if not self.__marks:
            return "No marks available"

        average = sum(self.__marks) / len(self.__marks)

        if average >= 80:
            grade = "A+"
        elif average >= 70:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 50:
            grade = "C"
        elif average >= 40:
            grade = "D"
        else:
            grade = "F"

        return f"Average: {average:.2f}, Grade: {grade}"

    def get_student_type(self):
        return "General Student"


# Inheritance
class UndergraduateStudent(Student):
    def __init__(
        self,
        name,
        student_id,
        email,
        age,
        department,
        semester,
        *marks
    ):
        super().__init__(
            name,
            student_id,
            email,
            age,
            department,
            *marks
        )
        self.semester = semester

    # Method Overriding
    def get_student_type(self):
        return "Undergraduate Student"

    def display_info(self):
        super().display_info()
        print(f"Semester: {self.semester}")


# Inheritance
class GraduateStudent(Student):
    def __init__(
        self,
        name,
        student_id,
        email,
        age,
        department,
        research_topic,
        *marks
    ):
        super().__init__(
            name,
            student_id,
            email,
            age,
            department,
            *marks
        )
        self.research_topic = research_topic

    # Method Overriding
    def get_student_type(self):
        return "Graduate Student"

    def display_info(self):
        super().display_info()
        print(f"Research Topic: {self.research_topic}")


# =========================================================
# Creating Objects
# =========================================================

student1 = Student(
    "Rahim",
    "S001",
    "rahim@example.com",
    20,
    "Computer Science",
    75,
    80,
    85
)

student2 = UndergraduateStudent(
    "Karim",
    "S002",
    "karim@example.com",
    21,
    "Software Engineering",
    6,
    70,
    78,
    82
)

student3 = GraduateStudent(
    "Nusrat",
    "S003",
    "nusrat@example.com",
    24,
    "Computer Science",
    "Artificial Intelligence",
    85,
    90,
    88
)


# =========================================================
# Display Information
# =========================================================

student1.display_info()
print("Student Type:", student1.get_student_type())
print("Result:", student1.calculate_result())

student2.display_info()
print("Student Type:", student2.get_student_type())
print("Result:", student2.calculate_result())

student3.display_info()
print("Student Type:", student3.get_student_type())
print("Result:", student3.calculate_result())


# =========================================================
# Method Overloading Demonstration
# =========================================================

print("\n--- Method Overloading Demonstration ---")

# Adding one mark
student1.add_marks(90)

# Adding multiple marks
student1.add_marks(88, 92, 95)

print("Updated Result:", student1.calculate_result())


# =========================================================
# Encapsulation Demonstration
# =========================================================

print("\n--- Encapsulation Demonstration ---")

# Accessing private email through getter
print("Student Email:", student1.get_email())

# Changing private email through setter
student1.set_email("newemail@example.com")

print("Updated Email:", student1.get_email())


# =========================================================
# Polymorphism Demonstration
# =========================================================

print("\n--- Polymorphism Demonstration ---")

students = [student1, student2, student3]

for student in students:
    print(
        f"{student.name} is a {student.get_student_type()}"
    )
