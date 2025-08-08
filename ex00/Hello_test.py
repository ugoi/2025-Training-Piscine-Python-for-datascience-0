from Hello import ft_list, ft_tuple, ft_set, ft_dict

# print(ft_list)
# print(ft_tuple)
# print(ft_set)
# print(ft_dict)


def test_ft_list_type():
    assert isinstance(ft_list, list)


def test_ft_list_value():
    assert ft_list == ["Hello", "World!"]


def test_ft_tuple_type():
    assert isinstance(ft_tuple, tuple)


def test_ft_tuple_value():
    assert ft_tuple == ("Hello", "France!")


def test_ft_set_type():
    assert isinstance(ft_set, set)


def test_ft_set_value():
    assert ft_set == {"Hello", "Paris!"}


def test_ft_dict_type():
    assert isinstance(ft_dict, dict)


def test_ft_dict_value():
    assert ft_dict == {'Hello': '42Paris!'}

