import types
import unittest
loader = unittest.TestLoader()

def test_it(func):
    class TestClass(unittest.TestCase):
        '''
        running 3 tests
        1. if function returns a generator
        2. one argument given
        3. two arguments given
        '''
        def test_instance(self):
            self.assertIsInstance(func(0,0), types.GeneratorType)
        def test_two_args(self):
            self.assertEqual(len(list(func(0,3))), 3)
        def test_one__arg(self):
            self.assertEqual(len(list(func(3))), 3)

    all_tests_from_class = loader.loadTestsFromTestCase(TestClass) # Return a suite of all test cases contained in testCaseClass
    unittest.TextTestRunner(verbosity=2).run(all_tests_from_class) # verbosity=2 for detailed output
    return func

@test_it
def custom_range(start,stop=0):
    if stop == 0:
        stop = start
        start = 0
    def start_custom_range(start,stop):
        yield start
        if start+1 < stop:
            yield from start_custom_range(start+1,stop)
    return start_custom_range(start,stop)

for each in custom_range(7):
    print(each)
