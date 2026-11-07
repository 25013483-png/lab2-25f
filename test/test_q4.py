import pytest
import sys
import util

def test_that_the_program_calculates_the_correct_volume(capsys):
    if 'q4' in sys.modules.keys():
        sys.modules.pop('q4')
    
    import q4    
    out, err = capsys.readouterr()

    expected = f"The volume of a square pyramid with base {q4.base}cm and height {q4.height}cm is {1/3*q4.base**2*q4.height}cm^3"
    assert out.strip() == expected, util.format_message("Your q4 code does not produce the correct output", expected, out)