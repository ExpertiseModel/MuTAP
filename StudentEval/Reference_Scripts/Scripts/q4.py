"""
Task: Sorting Tuples
Can we sort items other than integers? For this question, you will be sorting tuples! We represent a person using a tuple (<gender>, <age>). Given a list of people, write a function sort_age that sorts the people and return a list in an order such that the older people are at the front of the list. An example of the list of people is [("M", 23), ("F", 19), ("M", 30)]. The sorted list would look like [("M", 30), ("M", 23), ("F", 19)]. You may assume that no two members in the list of people are of the same age.
"""


def sort_age(lst):
    for i in range(0, len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i][1] < lst[j][1]:
                tmp = lst[i]
                lst[i] = lst[j]
                lst[j] = tmp
    return lst



print(sort_age([("M", 23), ("F", 19), ("M", 30), ("F", 25)])  ==[("M", 30), ("M", 23), ("F", 25), ("F", 19)])