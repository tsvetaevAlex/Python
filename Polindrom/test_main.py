import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from polindrom_pkg.polindrom import is_polindrom

def test_palindrom_true():
    assert is_polindrom("madam") == True, "is_polindrom 1st assert test passed"
    print ("is_polindrom 1st of 3 assert test passed")
def test_palindrom_false():
    assert is_polindrom("hello") == False, "is_polindrom 2nd assert test passed"
    print ("is_polindrom 2bd of 3 assert test passed")
def test_palindrom_single_letter():
    assert is_polindrom("a") == True
    print ("is_polindrom 3rd of 3 assert test passed")