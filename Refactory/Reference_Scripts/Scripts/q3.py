"""
Task: Duplicate elimination
Write a function remove_extras(lst) that takes in a list and returns a new list with all repeated occurrences of any element removed. For example, remove_extras([5, 2, 1, 2, 3]) returns the list [5, 2, 1, 3].
"""


def remove_extras(lst):
    newlist = []
    for i in lst:
        if i not in newlist:
            newlist.append(i)
    return newlist
