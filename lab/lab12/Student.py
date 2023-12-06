class Course:
    def __init__(self, title, code, credit):
        self.title = title
        self.course_id = code
        self.credit = credit


class Teacher:
    def __init__(self, firstname, lastname, id):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id

    def __str__(self):
        return f'{self.firstname} {self.lastname} ({self.id})'


class Major:
    def __init__(self, id, name, faculty):
        self.id = id
        self.name = name
        self.faculty = faculty

    def __str__(self):
        return f'{self.name} {self.faculty} ({self.id})'


class Student:
    def __init__(self, id, firstname, lastname):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.courses = []
        self.num_course = 0
        self.total_credit = 0
        self.advisor = None
        self.major = None

    def add_course(self, course):
        if course not in self.courses and self.total_credit + course.credit <= 25:
            self.courses.append(course)
            self.num_course += 1
            self.total_credit += course.credit
            return True
        return False

    def drop_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            self.num_course -= 1
            self.total_credit -= course.credit
            return True
        return False

    def set_advisor(self, advisor):
        self.advisor = advisor

    def set_major(self, major):
        self.major = major

    def __str__(self):
        student_info = (f'Student ID: {self.id}\n'
                        f'Name: {self.firstname} {self.lastname}\n'
                        f'Major: {self.major}\n'
                        f'Advisor: {self.advisor}\n'
                        f'Courses: ')
        for course in self.courses:
            student_info += course.course_id + ' '
        return student_info


# Create a Major object
major = Major("E17", "Software & Knowledge Engineering", "Engineering")

# Create a Teacher object
advisor = Teacher("Preeda", "Lerdpongvipusana", "E901")

# Create Course objects
courses = [
    Course("Course1", "01219111", 3),
    Course("Course2", "01219113", 4),
    Course("Course3", "01219245", 3),
    Course("Course4", "01219221", 4),
    Course("Course5", "01204212", 3),
    Course("Course6", "01219213", 4),
    Course("Course7", "01420113", 3),
    Course("Course8", "01420114", 4),
    Course("Course9", "01420111", 3)
]

# Create a Student object
student = Student("5610546231", "Chinnaporn", "Soonue")

# Set the major and advisor for the student
student.set_major(major)
student.set_advisor(advisor)

# Add courses to the student
for course in courses:
    student.add_course(course)

# Print the student information
print(student)
