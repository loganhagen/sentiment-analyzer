"""PyTest example to see if PyTest works in GitLab CI Pipeline"""

def func(test_var):
    """function"""
    return test_var + 1

def test_answer():
    """Function test"""
    assert func(3) == 4
