import os
import unittest
import progress_sheet as test_subject
loader = unittest.TestLoader()

def test_it(func):
    class TestClass(unittest.TestCase):
        '''running predefined tests'''
        def setUp(self): 
            self.student = test_subject.Student("test_student")
            self.teacher = test_subject.Teacher("")
            self.dean = test_subject.Deanery()
            self.student.save_progress()
            self.student.set_standard_curriculum()
            self.teacher.assign_mark(self.student,'Python','Infopulse Python course',5)
        
        def test_create_student(self):
            self.assertEqual(self.student.__class__, test_subject.Student)
        def test_create_teacher(self):
            self.assertEqual(self.teacher.__class__, test_subject.Teacher)
        def test_create_dean(self):
            self.assertEqual(self.dean.__class__, test_subject.Deanery)
        def test_save_student_progress_to_file(self):
            self.assertEqual(os.path.exists(f'.\json\{self.student.name}.json'), True)
            
        def test_set_student_standard_curriculum(self):
            self.assertIsInstance(self.student.progress['English'], type({}))
            self.assertIsInstance(self.student.progress['Python'], type({}))
            self.assertIsInstance(self.student.progress['Soft skills'], type({}))
        def test_mark_assign_by_teacher(self):
            self.assertEqual(self.student.progress['Python']['Infopulse Python course'][self.teacher.name], 5)
        def test_dean_know_student_average_score(self):
            self.assertEqual(self.dean.student_average_score(self.student), ('test_student', 1, 5.0)) #name,n of tests, score             
            
    all_tests_from_class = loader.loadTestsFromTestCase(TestClass) # Return a suite of all test cases contained in testCaseClass
    unittest.TextTestRunner(verbosity=2).run(all_tests_from_class) # verbosity=2 for detailed output
    return func

@test_it
def main():
    pass
