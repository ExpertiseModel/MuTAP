"""This code should be run from the root of the contest-problems repo. 
It saves all the problems in the repo as pickle files in the output directory."""

import io
import sys

import riegeli

import contest_problem_pb2
import pickle


def _all_problems(filenames):
    """Iterates through all ContestProblems in filenames."""
    for filename in filenames:
        reader = riegeli.RecordReader(
            io.FileIO(filename, mode="rb"),
        )
        for problem in reader.read_messages(contest_problem_pb2.ContestProblem):
            yield problem


def _print_names_and_sources(filenames):
    """Prints the names and sources of all ContestProblems in filenames."""
    for problem in _all_problems(filenames):
        data = {}
        # print(
        # contest_problem_pb2.ContestProblem.Source.Name(problem.source),
        # problem.name)
        name = problem.name
        data["source"] = contest_problem_pb2.ContestProblem.Source.Name(problem.source)
        data["name"] = name
        data["description"] = problem.description
        pub_test = {}
        for t in problem.public_tests:
            pub_test["input"] = t.input
            pub_test["output"] = t.output

        data["public_tests"] = pub_test

        priv_test = {}
        for t in problem.private_tests:
            priv_test["input"] = t.input
            priv_test["output"] = t.output

        data["private_tests"] = priv_test

        gen_test = {}
        for t in problem.generated_tests:
            gen_test["input"] = t.input
            gen_test["output"] = t.output

        data["generated_tests"] = gen_test

        solutions = {}
        for i, s in enumerate(problem.solutions):
            if s.language in {1, 3}:
                solutions[i] = s.solution

        data["solutions"] = solutions

        pickle.dump(
            data,
            open(
                ("/home/arghavan/code_contests/output_py_validation/" + name + ".pickle"),
                "wb",
            ),
        )


if __name__ == "__main__":
    _print_names_and_sources(sys.argv[1:])
