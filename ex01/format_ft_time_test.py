import datetime
from format_ft_time import format_date, format_seconds_since


def test_print_seconds_since():
    assert (
        format_seconds_since(1755717880.8326)
        == "Seconds since January 1, 1970: 1,755,717,880.8326 or 1.76e+09 in scientific notation"
    )


def test_format_date():
    date = datetime.datetime.strptime("Aug 20 2025", "%b %d %Y")
    assert format_date(date) == "Aug 20 2025"
