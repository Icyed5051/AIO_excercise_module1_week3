class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    def describe(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        return f"Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}"

class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        return f"Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}"

class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        return f"Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}"

class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def describe(self):
        description = f"Ward Name: {self.name}\n"
        for person in self.people:
            description += person.describe() + "\n"
        return description

    def count_doctor(self):
        return sum(1 for person in self.people if isinstance(person, Doctor))

    def sort_age(self):
        self.people.sort(key=lambda person: person.yob)

    def compute_average(self):
        teachers = [person for person in self.people if isinstance(person, Teacher)]
        if not teachers:
            return None
        average_yob = sum(teacher.yob for teacher in teachers) / len(teachers)
        return average_yob

student1 = Student(name="studentA", yob=2010, grade="7")
print(student1.describe())

teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
print(teacher1.describe())

doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
print(doctor1.describe())

teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")

ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)

print(ward1.describe())


print(f"Number of doctors: {ward1.count_doctor()}")
# >> Number of doctors: 2

print("\nAfter sorting Age of Ward1 people")
ward1.sort_age()
print(ward1.describe())


print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")

