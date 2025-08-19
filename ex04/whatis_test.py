import pytest
from whatis import whatis

outputs = {
    "even": "I'm Even.\n",
    "odd": "I'm Odd.\n",
    "empty": "",
    "err_not_int": "AssertionError: argument is not an integer\n",
    "err_too_many_args": "AssertionError: more than one argument is provided\n",
}


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (["whatis.py", "14"], outputs["even"]),
        (["whatis.py", "-5"], outputs["odd"]),
        (["whatis.py"], outputs["empty"]),
        (["whatis.py", "0"], outputs["even"]),
        (["whatis.py", "Hi!"], outputs["err_not_int"]),
        (["whatis.py", "13", "5"], outputs["err_too_many_args"]),
    ],
)
def test_whatis(capfd, test_input, expected):
    argv = test_input
    whatis(argv)
    captured = capfd.readouterr()
    assert captured.out == expected
