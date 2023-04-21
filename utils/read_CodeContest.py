import pickle
import os
import re


# the directory of one sample pickle file
directory = "/Users/ahvra/Codes/Copilot-Unit-Test-Generation/CodeContest/output_py_solutions/6_E. Exposition.pickle"

# Load files in pickle format. There is a seperate pickle file per each developer.
def open_file(file_path):
    with open(file_path, "rb") as picklefile:
        reader = pickle.load(picklefile)
    return reader


# print description, solution and tests for the problem in this pickle file


def print_data(file_path):
    data = open_file(file_path)
    print("Description: ", data["description"])
    Human_solution = []
    for s in data["solutions"]:
        Human_solution.append(data["solutions"][s])
        print("Solution sample: ", data["solutions"][s])
    print("Public Test: ", data["public_tests"]["input"])
    print("Generated Test: ", data["generated_tests"]["input"])


print_data(directory)
