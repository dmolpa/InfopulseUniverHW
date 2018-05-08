import json
import os

class Deanery():
    '''
    student_average_score(student-object)
    print_student_average_score(student-object)    # prints formatted string
    overall_statistics(*students-objects)
    print_overall_statistics(*students-objects)    # prints formatted string
    '''    
    def __init__(self):
        pass
    
    def student_average_score(self,student):
        student_marks={}
        average_mark = 0
        tests_taken = 0
        for subject,test_names in student.progress.items():
            for test, mark in test_names.items():
                for teacher_sign, mark in mark.items():
                    if mark > 2 and mark < 6:
                        average_mark += mark
                        tests_taken += 1
        if average_mark != 0:
            return (student.name,tests_taken,average_mark/tests_taken)
        else:
            return 'No marks'
    
    def print_student_average_score(self,student):
        score_tuple = self.student_average_score(student)
        print(f'Student {score_tuple[0]} attempted \t{score_tuple[1]} tests. Average score is: \t{round(score_tuple[2],1)}.')
    
    def overall_statistics(self,*students):
        overall_stats = []
        if len(students) == 1:
            self.student_average_score(students)
        elif len(students) >= 1:
            for each in students:
                overall_stats.append(self.student_average_score(each))  # get (student.name,tests_attempted,average_score)
        else:
            return 'Statistics is empty'
        return overall_stats
    
    def print_overall_statistics(self,*students):
        result = []
        for each in students:
            result.append(self.student_average_score(each))
        print('*** Overall students statistics ***')
        for each in result:
            print(f'{each[0]} attempted \t{each[1]} tests. His average score is \t{round(each[2],1)}.')
            
class Teacher():
    '''
    init with name
    methods:
    assign_mark(student,subject,test,mark)          
    view_evaluated_students()                       # prints formatted string. Students evaluated by current teacher.   
    '''
    def __init__(self,name):
        self.name = name
        self.evaluated_students = set()             # set(); stores objects; students which received a mark from self.Teacher
    
    def assign_mark(self,student,subject,test,mark):
        '''
        (self,student,subject,test,mark)
        (    ,object ,str    ,str ,int or float)
        '''
        student.progress[subject].update({test:{self.name:mark}})
        self.evaluated_students.add(student)                # adding student to set() after evaluation
    
    def view_evaluated_students(self):
        print(f'{self.name} had evaluated:' )
        for each in self.evaluated_students:
            print(f'  {each.name}')
            
class Student():
    '''
    init instance with name
    var self.progress is a dictionary:                      # stores most of data
    {subject:
        {test:
            {teacher:score},
        {test:
            {teacher:score}}}}
    methods:
    assign_classes(*subjects)                             # sets subjects names which holds nested dicts as values
    tests_attempted(subject,*tests)                         # sets tests names for given subject which holds nested dicts
    view_progress()
    save_progress()                                         # saves progress to dictionary. self.name.json
    load_progress()                                         # from json file into self.progress
    set_standard_curriculum()                               # assigns basic(hardcoded) set of subjects and tests.
    '''
    
    def __init__(self,name):
        self.name = name
        self.progress = {}                                  # stores most of data
    
    def assign_classes(self,*subjects):
        '''accepts subject names(str) ads it as keys to self.progress dict'''
        for i in range(len(subjects)):
            self.progress.update({subjects[i]:{}})
    
    def tests_attempted(self,subject,*tests):
        '''
        expect a subject name(str) and tests(str) been attempted
        adds test names as keys to dicts nested under given subject
        sets marks == 0
        '''
        for test in tests:
            try:
                self.progress[subject].update({test:{}})
            except KeyError:
                print('key error')
    
    def view_progress(self):
        '''prints out subject names on separate lines followed by tests and marks'''
        print(f"*** {self.name}'s academic progress is:\n----------------------------")
        for subject, test in self.progress.items():
            print(f'{subject}')
            for test_name, mark in test.items():
                for teachers_sign, mark in mark.items():
                    print(f'  {test_name} test score is:\t{mark} :by {teachers_sign}')
            print('-'*30)
        print('*'*30+'\n')
    
    def save_progress(self):
        with open(f'.\json\{self.name}.json', 'w') as file:
            json.dump(self.progress, file)
    
    def load_progress(self):
        with open(f'.\json\{self.name}.json', 'r') as file:
            check = input(f"Loading {self.name}'s progress from file, this will overwrite unsaved progress. Proceed? yes|no: ")
            check = check.lower()
            if check == 'yes' or check =='y':
                self.progress = json.load(file)
                print('Progress loaded from file.')
            else:
                print('load interupted')

    def load_n_view_progress(self):
        with open(f'.\json\{self.name}.json', 'r') as file:
            check = input(f"Loading {self.name}'s progress from file, this will overwrite unsaved progress. Proceed? yes|no: ")
            check = check.lower()
            if check == 'yes' or check =='y':
                self.progress = json.load(file)
                print('Progress loaded from file.')
                self.view_progress()
            else:
                print('load interupted')
    
    def set_standard_curriculum(self):
        self.assign_classes('Python','English','Soft skills')
        self.tests_attempted('English','Speaking','Listening','Reading','Writing')
        self.tests_attempted('Python','Infopulse Python Course')
        self.tests_attempted('Soft skills','Cooperation')

if not os.path.exists('.\json'):
    os.mkdir('.\json')