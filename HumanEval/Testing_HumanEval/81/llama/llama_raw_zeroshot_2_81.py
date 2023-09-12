[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def numerical_letter_grade(grades):
    

   
    letter_grade = []
    for gpa in grades:
        if gpa == 4.0:
            letter_grade.append("A+")
        elif gpa > 3.7:
            letter_grade.append("A")
        elif gpa > 3.3:
            letter_grade.append("A-")
        elif gpa > 3.0:
            letter_grade.append("B+")
        elif gpa > 2.7:
            letter_grade.append("B")
        elif gpa > 2.3:
            letter_grade.append("B-")
        elif gpa > 2.0:
            letter_grade.append("C+")
        elif gpa > 1.7:
            letter_grade.append("C")
        elif gpa > 1.3:
            letter_grade.append("C-")
        elif gpa > 1.0:
            letter_grade.append("D+")
        elif gpa > 0.7:
            letter_grade.append("D")
        elif gpa > 0.0:
            letter_grade.append("D-")
        else:
            letter_grade.append("E")
    return letter_grade


# test case
def test():
    assert [/INST]  To generate test cases for the `numerical_letter_grade` function, we can use the `unittest` module in Python. Here's an example of how to write test cases for the function:
```
import unittest

class TestNumericalLetterGrade(unittest.TestCase):
    def test_empty_grades(self):
        grades = []
        result = numerical_letter_grade(grades)
        self.assertEqual(result, ["E"])

    def test_low_grades(self):
        grades = [2.0]
        result = numerical_letter_grade(grades)
        self.assertEqual(result, ["D-"])

    def test_medium_grades(self):
        grades = [3.2, 3.5, 3.8]
        result = numerical_letter_grade(grades)
        self.assertEqual(result, ["B+", "B", "B-"])

    def test_high_grades(self):
        grades = [4.1, 4.3, 4