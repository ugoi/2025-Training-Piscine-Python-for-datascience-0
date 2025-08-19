import sys


def whatisinput(input: str):
    try:
        number = int(input)
    except:
        print("AssertionError: argument is not an integer")
        return

    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
    return


def whatis(argv: list[str]):
    argv_len = len(argv)
    if argv_len > 2:
        print("AssertionError: more than one argument is provided")
        return
    elif argv_len < 2:
        return
    input = argv[1]
    whatisinput(input)


def main():
    whatis(sys.argv)


if __name__ == "__main__":
    main()
