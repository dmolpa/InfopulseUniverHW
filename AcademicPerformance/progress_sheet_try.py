from progress_sheet import *

#--- STUDENTS ---------------------------------------------------------------------------------
me = Student('Dmytro')                                                              # instance init
me.set_standard_curriculum()                                                        # sets basic curriculum
me.tests_attempted('Python','Udemy complete bootcamp','Udemy Python mega course')   # custom tests attempted
#--- basic student instances
student_1 = Student('Guido')
student_2 = Student('Monty')
student_3 = Student('Python')
student_1.set_standard_curriculum()
student_2.set_standard_curriculum()
student_3.set_standard_curriculum()


#--- TEACHERS ----------------------------------------------------------------------------------
alex = Teacher('Alexander Galkin')
ielts = Teacher('British Council')
jose = Teacher('Jose Portilla')
ardit = Teacher('Ardit Sulce')
soft = Teacher('Life')
#--- teacher.method(student,'subject_name','test_name',score) teacher's name is added at the end
ielts.assign_mark(me,'English','Speaking',7.0)
ielts.assign_mark(me,'English','Listening',7.5)
ielts.assign_mark(me,'English','Reading',6.5)
ielts.assign_mark(me,'English','Writing',6.0)
alex.assign_mark(me,'Python','Infopulse Python course',4)
jose.assign_mark(me,'Python','Udemy complete bootcamp',5)
ardit.assign_mark(me,'Python','Udemy Python mega course',4)
soft.assign_mark(me,'Soft skills','Cooperation',4)

ielts.assign_mark(student_1,'English','Speaking',5)
ielts.assign_mark(student_1,'English','Listening',5)
ielts.assign_mark(student_1,'English','Reading',5)
ielts.assign_mark(student_1,'English','Writing',5)
alex.assign_mark(student_1,'Python','Infopulse Python course',5)
soft.assign_mark(student_1,'Soft skills','Cooperation',4)

ielts.assign_mark(student_2,'English','Speaking',7.0)
alex.assign_mark(student_2,'Python','Infopulse Python course',4)
soft.assign_mark(student_2,'Soft skills','Cooperation',4)

ielts.assign_mark(student_3,'English','Speaking',7.0)
alex.assign_mark(student_3,'Python','Infopulse Python course',5)
soft.assign_mark(student_3,'Soft skills','Cooperation',4)
#---


#--- DEANERY ---------------------------------------------------------------------------------
dean = Deanery()
#--- dean view methods
dean.print_student_average_score(me)
dean.print_student_average_score(student_1)
print('-'*70+'\n')
dean.print_overall_statistics(me,student_1,student_2,student_3)

#--- SAVE-LOAD METHODS ---------------------------------------------------------------------------------
print('-'*70+'\n')
me.save_progress()
student_1.save_progress()
student_2.save_progress()
student_3.save_progress()
#me.load_progress()

#--- VIEW AND PRINT METHODS  -----------------------------------------------------------------
me.load_n_view_progress()
student_1.load_n_view_progress()
student_2.load_n_view_progress()
student_3.load_n_view_progress()
#--- view students evaluated by specific teacher
print('-'*70+'\n')
alex.view_evaluated_students()
ielts.view_evaluated_students()
#jose.view_evaluated_students()
#ardit.view_evaluated_students()
#soft.view_evaluated_students()
#
