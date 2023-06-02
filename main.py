class Student:
    def register(self):
        self.name = input('Enter Student Name : ')
        self.sNum = input('Enter Student Number : ')


class Teacher:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Course:
    def __init__(self, name, teacherId, teacher, listStudent):
        self.name = name
        self.id = teacherId
        self.teacher = teacher
        self.listStudent = listStudent


student1 = Student()
student1.register()
student2 = Student()
student2.register()
student3 = Student()
student3.register()
student4 = Student()
student4.register()

teacher1 = Teacher('Ali', 1)
teacher2 = Teacher('Mohammad', 2)
teacher3 = Teacher('Naser', 3)

flutterCourse = Course('Flutter', 1, teacher1 , [student1, student3])
pythonCourse = Course('Python', 2, teacher2, [student4])
kotlinCourse = Course('Kotlin', 3, teacher3, [student2, student1])

flutterStudents = []
pythonStudents = []
kotlinStudents = []

for i in flutterCourse.listStudent:
    flutterStudents.append(i.name)

for i in pythonCourse.listStudent:
    pythonStudents.append(i.name)

for i in kotlinCourse.listStudent:
    kotlinStudents.append(i.name)


print(str(flutterCourse.id) +') Course Name : ' + flutterCourse.name + ' | Course Teacher : ' + flutterCourse.teacher.name + ' | Course Students : ' + str(flutterStudents))
print(str(pythonCourse.id) +') Course Name : ' + pythonCourse.name + ' | Course Teacher : ' + pythonCourse.teacher.name + ' | Course Students : ' + str(pythonStudents))
print(str(kotlinCourse.id) +') Course Name : ' + kotlinCourse.name + ' | Course Teacher : ' + kotlinCourse.teacher.name + ' | Course Students : ' + str(kotlinStudents))

