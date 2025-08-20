import pytest
from Hello import ft_list, ft_tuple, ft_set, ft_dict


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (ft_list, list),
        (ft_tuple, tuple),
        (ft_set, set),
        (ft_dict, dict),
    ],
)
def test_ft_list_type(test_input, expected):
    assert isinstance(test_input, expected)


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (ft_list, ["Hello", "World!"]),
        (ft_tuple, ("Hello", "France!")),
        (ft_set, {"Hello", "Paris!"}),
        (ft_dict, {"Hello": "42Paris!"}),
    ],
)
def test_ft_list_value(test_input, expected):
    assert test_input == expected
