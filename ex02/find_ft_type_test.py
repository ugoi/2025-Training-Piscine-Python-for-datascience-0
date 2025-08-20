import pytest
from find_ft_type import all_thing_is_obj

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}


@pytest.mark.parametrize(
    "test_input, expected_stdout, expected",
    [
        (ft_list, "List : <class 'list'>\n", 42),
        (ft_tuple, "Tuple : <class 'tuple'>\n", 42),
        (ft_set, "Set : <class 'set'>\n", 42),
        (ft_dict, "Dict : <class 'dict'>\n", 42),
        ("Brian", "Brian is in the kitchen : <class 'str'>\n", 42),
        (10, "Type not found\n", 42),
    ],
)
def test_all_thing_is_obj_prints_list_type(
    capfd, test_input, expected_stdout, expected
):
    assert all_thing_is_obj(test_input) == expected
    captured = capfd.readouterr()
    assert captured.out == expected_stdout
