from find_ft_type import all_thing_is_obj

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}


def test_all_thing_is_obj_returns_42():
    assert all_thing_is_obj(ft_list) == 42


def test_all_thing_is_obj_prints_list_type(capfd):
    all_thing_is_obj(ft_list) == 42
    captured = capfd.readouterr()
    assert captured.out == "List : <class 'list'>\n"


def test_all_thing_is_obj_prints_tuple_type(capfd):
    all_thing_is_obj(ft_tuple) == 42
    captured = capfd.readouterr()
    assert captured.out == "Tuple : <class 'tuple'>\n"


def test_all_thing_is_obj_prints_set_type(capfd):
    all_thing_is_obj(ft_set) == 42
    captured = capfd.readouterr()
    assert captured.out == "Set : <class 'set'>\n"


def test_all_thing_is_obj_prints_dict_type(capfd):
    all_thing_is_obj(ft_dict) == 42
    captured = capfd.readouterr()
    assert captured.out == "Dict : <class 'dict'>\n"

def test_all_thing_is_obj_prints_str_type(capfd):
    all_thing_is_obj("Brian") == 42
    captured = capfd.readouterr()
    assert captured.out == "Brian is in the kitchen : <class 'str'>\n"

def test_all_thing_is_obj_passing_an_int_as_arg_should_return_type_not_found(capfd):
    all_thing_is_obj(10) == 42
    captured = capfd.readouterr()
    assert captured.out == "Type not found\n"