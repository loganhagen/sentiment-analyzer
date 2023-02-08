"""PyTest example to see if PyTest works in GitLab CI Pipeline"""

def func(x):
    """function"""
    return x + 1

def test_answer():
    """Function test"""
    assert func(3) == 4