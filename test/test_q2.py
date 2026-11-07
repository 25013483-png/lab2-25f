import pytest
import sys


def test_that_the_file_run_without_error():
  if 'q2' in sys.modules.keys():
    sys.modules.pop('q2')
  import q2
