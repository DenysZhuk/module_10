import sys
from functions import add_contact, change_contact, show_all, phone, help_me, delete_number

commands = {
    "hello": lambda *_: "How can I help you?",
    "add": add_contact,
    "change": change_contact,
    "delete": delete_number,
    "phone": phone,
    "show": show_all,
    "help_me": help_me,
    "empty": lambda *_: "Use 'help' command to know what I can.",
    "exit": lambda *_: sys.exit(),
    "close": lambda *_: sys.exit(),
    "goodbye": lambda *_: sys.exit(),
    0: lambda *_: "Sorry I can't understand you. Try 'help' command to see what I can.",
}


def def_mod(string: str):
    try:
        mods = {
            ".": "exit",
            "hello": "hello",
            "goodbye": "goodbye",
            "close": "exit",
            "exit": "exit",
            "add": "add",
            "delete": "delete",
            "phone": "phone",
            "show": "show",
            "help": "help_me",
            "change": "change"
        }
        if not string:
            return "empty", ""
        for key_word in mods.keys():
            if key_word in string.lower():
                return mods[key_word], string.replace(key_word, "")
        return 0, ""
    except Exception as err:
        return err