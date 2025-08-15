from NULL_not_found import NULL_not_found

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False


def test_NULL_not_found_returns_0():
    assert NULL_not_found(Nothing) == 0


def test_NULL_not_found_prints_nan_type(capfd):
    NULL_not_found(Nothing) == 0
    captured = capfd.readouterr()
    assert captured.out == "Nothing : None <class 'NoneType'>\n"


def test_NULL_not_found_prints_nan_type(capfd):
    NULL_not_found(Garlic) == 0
    captured = capfd.readouterr()
    assert captured.out == "Cheese : nan <class 'float'>\n"


def test_NULL_not_found_prints_float_type(capfd):
    NULL_not_found(Zero) == 0
    captured = capfd.readouterr()
    assert captured.out == "Zero : 0 <class 'int'>\n"


def test_NULL_not_found_prints_set_type(capfd):
    NULL_not_found(Empty) == 0
    captured = capfd.readouterr()
    assert captured.out == "Empty :  <class 'str'>\n"


def test_NULL_not_found_prints_dict_type(capfd):
    NULL_not_found(Fake) == 0
    captured = capfd.readouterr()
    assert captured.out == "Fake : False <class 'bool'>\n"


def test_NULL_not_found_prints_str_type(capfd):
    assert NULL_not_found("Brian") == 1
    captured = capfd.readouterr()
    assert captured.out == "Type not found\n"
