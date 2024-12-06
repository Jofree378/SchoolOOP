class Student:

    # --< Список студентов пополняющийся при создании нового экземпляра класса -->
    students = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.students += [self]

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lector(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if grade in range(1, 11):
                if course in lector.grade_feedback:
                    lector.grade_feedback[course] += [grade]
                else:
                    lector.grade_feedback[course] = [grade]
            else:
                return 'Некорректная оценка'
        else:
            return 'Ошибка'

    def getGrades(self):
        return self.grades

    def avg_rate(self):
        sum_rate = 0
        rate_count = 0
        for course, grade in self.grades.items():
            sum_rate += sum(grade)
            rate_count += len(grade)
        return sum_rate / rate_count

    def __str__(self):
        return f'''
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за домашние задания: {self.avg_rate():.1f}
        Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
        Завершенные курсы: {', '.join(self.finished_courses)}'''

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.avg_rate() < other.avg_rate()

    def __le__(self, other):
        if isinstance(other, Student):
            return self.avg_rate() <= other.avg_rate()

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.avg_rate() == other.avg_rate()

    def __ne__(self, other):
        if isinstance(other, Student):
            return self.avg_rate() != other.avg_rate()

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.avg_rate() >= other.avg_rate()

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.avg_rate() > other.avg_rate()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):

    # --< Список лекторов пополняющийся при создании нового экземпляра класса -->
    lectors = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade_feedback = {}
        Lecturer.lectors += [self]

    def get_grade_feedback(self):
        return self.grade_feedback

    def avg_rate(self):
        sum_rate = 0
        rate_count = 0
        for course, grade in self.grade_feedback.items():
            sum_rate += sum(grade)
            rate_count += len(grade)
        return sum_rate / rate_count

    def __str__(self):
        return f'''
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за лекции: {self.avg_rate():.1f}
        '''

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_rate() < other.avg_rate()

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_rate() <= other.avg_rate()

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_rate() == other.avg_rate()

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_rate() != other.avg_rate()

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_rate() >= other.avg_rate()

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_rate() > other.avg_rate()



class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'''
        Имя: {self.name}
        Фамилия: {self.surname}'''


def avg_all_students(all_students, course):
    sum_rate = 0
    rate_count = 0
    for student in all_students:
        sum_rate += sum(student.grades[course])
        rate_count += len(student.grades[course])
    return round(sum_rate / rate_count, 1)

def avg_all_lectors(all_lectors, course):
    sum_rate = 0
    rate_count = 0
    for lector in all_lectors:
        sum_rate += sum(lector.grade_feedback[course])
        rate_count += len(lector.grade_feedback[course])
    return round(sum_rate / rate_count, 1)



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.add_courses('Введение в программирование')

best_student2 = Student('Ruoy2', 'Eman2', 'your_gender')
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['Git']


cool_lector = Lecturer('Some', 'Buddy')
cool_lector.courses_attached += ['Python']

cool_lector2 = Lecturer('Some2', 'Buddy2')
cool_lector2.courses_attached += ['Python']

best_student.rate_lector(cool_lector2, 'Python', 3)
best_student.rate_lector(cool_lector2, 'Python', 5)

best_student.rate_lector(cool_lector, 'Python', 5)
best_student.rate_lector(cool_lector, 'Python', 3)


review = Reviewer('some', 'bddy')
review2 = Reviewer('some', 'bddy')

review.courses_attached += ['Python']
review.courses_attached += ['Git']

review2.courses_attached += ['Python']
review2.courses_attached += ['Git']

review.rate_hw(best_student, 'Git', 10)
review.rate_hw(best_student, 'Git', 6)

review2.rate_hw(best_student2, 'Git', 10)
review2.rate_hw(best_student2, 'Git', 6)



#--< Вывод функций расчитывающих среднее значение -->

print(avg_all_students(Student.students, 'Git'))
print(avg_all_lectors(Lecturer.lectors, 'Python'))


#print(best_student.getGrades())

#--< Проверка задания 2 -->

# print(review)
# print(cool_mentor)
# print(best_student)

#--< Проверка сравнение лекторов -->

# print(cool_lector > cool_lector2)
# print(cool_lector >= cool_lector2)
# print(cool_lector == cool_lector2)
# print(cool_lector != cool_lector2)
# print(cool_lector < cool_lector2)
# print(cool_lector <= cool_lector2)

#--< Проверка сравнение студентов -->

# print(best_student > best_student2)
# print(best_student >= best_student2)
# print(best_student == best_student2)
# print(best_student != best_student2)
# print(best_student < best_student2)
# print(best_student <= best_student2)



