import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from main import is_polindrom

def test_palindrom_true():
    assert is_polindrom("madam") == True

def test_palindrom_false():
    assert is_polindrom("hello") == False

def test_palindrom_single_letter():
    assert is_polindrom("a") == True