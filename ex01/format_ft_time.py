from datetime import datetime


def get_seconds_since_epoch():
    now = datetime.now()
    epoch = datetime(1970, 1, 1)
    delta = now - epoch
    return delta.total_seconds()


def get_current_date():
    now = datetime.now()
    date_format = now.strftime("%b %d %Y")
    return date_format


seconds_since_epoch = get_seconds_since_epoch()
current_date = get_current_date()

print(
    "Seconds since January 1, 1970: {} or {} in scientific notation".format(
        "{0:,.4f}".format(seconds_since_epoch), "{:.2e}".format(seconds_since_epoch)
    )
)
print(current_date)
