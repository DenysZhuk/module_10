import classes
from commands import commands, def_mod
import sys


def main():
    print("Hello I`m your contact bot!")
    print("What you want me to do?")
    book = classes.AddressBook()
    while True:
        command = input()
        mode, data = def_mod(command)
        output = commands.get(mode)(book, data)
        print(output)
        if output == "Good bye!":
            sys.exit()


if __name__ == "__main__":
    main()