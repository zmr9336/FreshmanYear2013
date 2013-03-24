import unittest
from frequency import *

# import the module(s) to be tested:
# from template import *

class TestTemplate(unittest.TestCase):

    # setUp - run prior to the start of each test case
    def setUp(self):
	# initialize test fixtures
        return

    def test_smoke(self):
        # very simple test to insure test framework is correct
        # replace this assert with meaningful test 
        self.assertTrue(1)

    # additional test_xxx methods follow....

    def test_emptyLine(self):
        #testing if the line is empty, then it will pass
        self.assertEqual(frequency('') , None)
	
if __name__ == '__main__':
    unittest.main()