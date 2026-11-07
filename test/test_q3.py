import sys

import pytest
import util


def test_that_output_is_correct(capsys):
  if 'q3' in sys.modules.keys():
    sys.modules.pop('q3')
  import q3
  out, err = capsys.readouterr()
  expected = "Feeling...HotHotHot!\n"
  assert out == expected, util.format_message(
      "Your q3 code does not produce the correct output. (Have you carefully checked for problems with case sensitivity, spaces, and newlines?)",
      expected, out)
