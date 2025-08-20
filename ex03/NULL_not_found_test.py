import pytest
from NULL_not_found import NULL_not_found

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False
Brian = "Brian"

SUCCESS = 0
FAIL = 1


@pytest.mark.parametrize(
    "test_input, expected_stdout, expected",
    [
        (Nothing, "Nothing : None <class 'NoneType'>\n", 0),
        (Garlic, "Cheese : nan <class 'float'>\n", 0),
        (Zero, "Zero : 0 <class 'int'>\n", 0),
        (Empty, "Empty :  <class 'str'>\n", 0),
        (Fake, "Fake : False <class 'bool'>\n", 0),
        (Brian, "Type not found\n", 1),
    ],
)
def test_NULL_not_found(capfd, test_input, expected_stdout, expected):
    assert NULL_not_found(test_input) == expected
    captured = capfd.readouterr()
    assert captured.out == expected_stdout
