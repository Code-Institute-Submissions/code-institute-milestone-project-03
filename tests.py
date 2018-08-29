import unittest, json
from types import IntType
from testfunctions import checkusername, checkanswer, nextriddle


with open("data/riddles.json") as riddles:
    RIDDLES = json.load(riddles)['riddles"]
    

class AnswerTests(unittest.TestCase):
    '''
    Asserts a known correct answer is checked as correct
    '''
    def test_correct_answer(self):
        self.assertTrue(
            check_answer(RIDDLES[3], "lawsuit"), 
            "Correct answer was checked as incorrect")
        
    '''
    Asserts an empty answer is checked as incorrect
    '''
    def test_empty_answer(self):
        self.assertFalse(
            check_answer(RIDDLES[7], ""), 
            "Empty answer was not marked as empty")
    

class RiddleTests(unittest.TestCase):
        
    '''
    Asserts that initial riddle is loaded correctly
    '''
    def test_initial_load(self):
        self.assertEqual(
            get_next_riddle(RIDDLES, None)["question"], 
            "What has a head, a tail, is brown, and has no legs?", 
            "First riddle did not load")
)


if __name__ == '__main__':
    unittest.main()
    