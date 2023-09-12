[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def sum_to_n(n: int):
    
    return sum(range(n + 1))




# test case
def test():
    assert [/INST]  Sure, here are some test cases for the `sum_to_n` function:

# Test 1: Basic case
def test_sum_to_1():
    assert sum_to_n(1) == 1

# Test 2: Edge case
def test_sum_to_n_edge_case():
    assert sum_to_n(0) == 0
    assert sum_to_n(-1) == 0

# Test 3: Negative input
def test_sum_to_n_negative():
    with pytest.raises(TypeError):
        sum_to_n(-2)

# Test 4: Large input
def test_sum_to_n_large():
    assert sum_to_n(100) == 5050

# Test 5: Testing the edge case of sum_to_n = n
def test_sum_to_n_edge_case_n():
    assert sum_to_n(5) == 15

# Test 6: Testing the edge case of sum_to_