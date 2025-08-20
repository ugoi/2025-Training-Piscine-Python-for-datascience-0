from datetime import datetime


def get_seconds_since_epoch():
    now = datetime.now()
    epoch = datetime(1970, 1, 1)
    delta = now - epoch
    return delta.total_seconds()


def format_date(date: datetime):
    return date.strftime("%b %d %Y")


def get_current_date():
    now = datetime.now()
    date_format = format_date(now)
    return date_format


def format_seconds_since(seconds: float):
    return "Seconds since January 1, 1970: {} or {} in scientific notation".format(
        "{0:,.4f}".format(seconds), "{:.2e}".format(seconds)
    )


seconds_since_epoch = get_seconds_since_epoch()
current_date = get_current_date()
formatted = format_seconds_since(seconds_since_epoch)
print(formatted)
print(current_date)
