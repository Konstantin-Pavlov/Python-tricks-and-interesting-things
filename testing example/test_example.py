'''
To run these tests using pytest, follow these steps:

Install pytest by running pip install pytest in your terminal.
Save the test file with a name starting with test_ (e.g., test_example.py).
Open a terminal and navigate to the directory where your test file is located.
Run pytest by executing pytest in the terminal.

note: save file after changing it
'''

def add(x, y):
    return x + y

def test_add_positive_numbers():
    result = add(2, 3)
    assert result == 5

def test_add_negative_numbers():
    result = add(-2, -3)
    assert result == -5

def test_add_mixed_numbers():
    result = add(5, -3)
    assert result == 2