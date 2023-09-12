
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
    assert numerical_letter_grade([]) == []


    assert numerical_letter_grade([2.0]) == ['C']


    assert numerical_letter_grade([3.2, 3.5, 3.8]) == ['B+', 'A-', 'A']
    assert numerical_letter_grade([4.1, 3.9, 3.5, 2.8, 2.3, 1.0]) == ['A', 'A', 'A-', 'B', 'C+', 'D']
    # Test the original function
    assert numerical_letter_grade([4.0, 3.7, 3.3, 2.7, 2.3, 1.0]) == ['A+', 'A-', 'B+', 'B-', 'C+', 'D']
    assert numerical_letter_grade([4.0, 3.5, 3.8, 3.2, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]) == ['A+', 'A-', 'A', 'B+', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E']
    assert numerical_letter_grade([3.2, 3.5, 3.8, 2.5]) == ['B+', 'A-', 'A', 'B-']
    assert numerical_letter_grade([3.5, 3.8, 4.2, 4.5]) == ['A-', 'A', 'A', 'A']
    assert numerical_letter_grade([4.0, 3.8, 3.5, 3.2, 3.0, 2.8, 2.5, 2.0, 1.8, 1.5, 1.0]) == ['A+', 'A', 'A-', 'B+', 'B', 'B', 'B-', 'C', 'C', 'C-', 'D']
    assert numerical_letter_grade([4.5]) == ['A']

    # Other tests remain the same
    assert numerical_letter_grade([]) == []
    assert numerical_letter_grade([2.0]) == ['C']
    assert numerical_letter_grade([3.2, 3.5, 3.8]) == ['B+', 'A-', 'A']
    assert numerical_letter_grade([4.1, 3.5, 3.8]) == ['A', 'A-', 'A']

    # Test that the function outputs the correct letter grade for a list with an element less than 4.0
    assert numerical_letter_grade([3.0, 2.5, 3.8]) == ['B', 'B-', 'A']
    assert numerical_letter_grade([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]) == ['E', 'D-', 'D', 'C-', 'C', 'B-', 'B', 'A-', 'A+']
    assert numerical_letter_grade([3.5, 3.8, 4.2, 4.5, 3.0, 2.5, 1.5, 0.5]) == ['A-', 'A', 'A', 'A', 'B', 'B-', 'C-', 'D-']
    # Test the modified logic
    assert numerical_letter_grade([3.0, 3.5, 3.8]) == ['B', 'A-', 'A']

    # Test the original logic
    assert numerical_letter_grade([2.0, 3.2, 3.5, 3.8]) == ['C', 'B+', 'A-', 'A']
    assert numerical_letter_grade([3.2, 2.7, 1.5, 4.0, 3.8, 1.1, 1.2, 0.8, 1.3]) == ['B+', 'B-', 'C-', 'A+', 'A', 'D+', 'D+', 'D', 'D+']
    assert numerical_letter_grade([1.5, 2.1, 2.7, 3.1, 3.5, 4.0, 4.5, 5.0, 5.5]) == ['C-', 'C+', 'B-', 'B+', 'A-', 'A+', 'A', 'A', 'A']
    assert numerical_letter_grade([4.5, 3.8, 3.1, 2.3, 1.8]) == ['A', 'A', 'B+', 'C+', 'C']
    assert numerical_letter_grade([2.5, 3.2, 3.8]) == ['B-', 'B+', 'A']
