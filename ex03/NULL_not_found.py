from types import NoneType


def isNaN(num):
    return num != num


def NULL_not_found(thing: any) -> int:
    if thing and (not isNaN(thing)):
        print("Type not found")
        return 1
    else:
        title = ""
        if isinstance(thing, NoneType):
            title = "Nothing"
        elif isinstance(thing, bool):
            title = "Fake"
        elif isinstance(thing, float):
            title = "Cheese"
        elif isinstance(thing, int):
            title = "Zero"
        elif isinstance(thing, str):
            title = "Empty"
        print(f"{title} : {thing} {type(thing)}")
    return 0
