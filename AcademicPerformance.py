class Statistics:
    def __init__(self):
        self.five = 0
        self.four = 0
        self.three = 0
        self.two = 0

    def __add__(self, other): #overload
        result = Statistics()
        result.five = self.five + other.five
        result.four = self.four + other.four
        result.three = self.three + other.three
        result.two = self.two + other.two
        return result

    def __str__(self): # convert to string

        return 'Five:\t%s\nFour:\t%s\nThree:\t%s\nTwo:\t%s' % (self.five,self.four,self.three,self.two)


# example
# statistics1 = Statistics()
# statistics2 = Statistics()
# statistics3 = statistics1 + statistics2
# == to uplisted statistics3 = statistics1.__add__(statistics2)

class Session:
    def __init__(self, session_name):
        self.name = session_name
        self.exam_list = []

    def add_exam(self, exam):
        self.exam_list.append(exam)

    def statistics(self):
        result_statistic = Statistics()
        for exam in self.exam_list:
            result_statistic += exam.statistics()
        return result_statistic

class Exam:
    def __init__(self, subject, date, teacher):
        self.subject = subject
        self.date = date
        self.teacher = teacher
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

    def statistics(self):
        result_statistics = Statistics()
        for mark in self.marks:
            if mark.value == 2:
                result_statistics.two += 1
            if mark.value == 3:
                result_statistics.three += 1
            if mark.value == 4:
                result_statistics.four += 1
            if mark.value == 5:
                result_statistics.five += 1
        return result_statistics

class Mark:
    def __init__(self, student, mark):
        self.student = student
        self.value = mark

class Student:
    def __init__(self, name):
        self.name = name

class Teacher:
    def __init__(self, name):
        self.name = name

class Subject:
    def __init__(self, name):
        self.name = name

teacher1 = Teacher('Teacher1')
student1 = Student('Student1')
student2 = Student('Student2')
student3 = Student('Student3')
math = Subject('Math')
exam = Exam(math,'today',teacher1)
exam.add_mark(Mark(student1,3))
exam.add_mark(Mark(student2,4))
exam.add_mark(Mark(student3,5))
session = Session('Spring 2018')
session.add_exam(exam)
statistics = session.statistics()
print(statistics)