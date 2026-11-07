import pytest
from q1 import *

def test_that_n_is_42():
  try:
    assert n == 42, "n must be assigned the value 42"
  except NameError:
    pytest.fail("You did not make a variable named n")
      

def test_that_tau_is_2pi():
  try:
    assert abs(tau - 6.28319) < 0.001, "tau must be assigned the value of two times pi"
  except NameError:
    pytest.fail("You did not make a variable named tau")

def test_that_school_is_sault_college():
  try:
    assert school == "Sault College", "school must be assigned the value  'Sault College'"
  except NameError:
    pytest.fail("You did not make a variable named school")