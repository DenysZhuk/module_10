from classes import *

no_name = "Sorry, I can't identify a contact's name."


def add_contact(book: AddressBook, data: str):
    name = input(f"Enter user name:{data}")
    phone_number = input("Give me phone please: ")
    if not name:
        return no_name
    elif name in book.data.keys():
        return f"Contact '{name}' already exists"
    else:
        record = Record(Name(name), [Phone(phone_number)] if phone_number else [])
        book.add_record(record)
        return f"Created contact '{name}': '{phone_number}'"


def change_contact(book: AddressBook, data: str):
    name = input(f"Enter user name:{data}")
    if name in book.data.keys():
        change_number = input("Enter new phone number: ")
        book[name] = change_number
        return f"Updated contact '{name}': '{change_number}'"
    else:
        print("Sorry, I can't identify a contact's name.")


def show_all(book: AddressBook, *_):
    for name, phone_number in book.data.items():
        print(f'{name}: {", ".join(phone.value for phone in phone_number.phones)}')


def phone(book: AddressBook, data: str):
    name = input(f"Enter user name:{data} ")
    if name in book.data.keys():
        return f"{name}: {', '.join([x.value for x in book.data.get(name).phones])}"
    else:
        return f"Contact '{name}' does not exists"


def delete_number(book: AddressBook, data: str):
    name = input(f"Enter user name you want to delete:{data} ")
    if name in book.data.keys():
        book.data[name] = Record(Name(name))
        return f"Done!"
    else:
        return f"Contact {name} does not exist."


def help_me(*_):
    return "Hello! I`m your contacts helper\n" \
           "Add new contact [Add]\n" \
           "Change number in existing contact [Change]\n" \
           "Delete contact [Delete]\n" \
           "Find number by name [Phone]\n" \
           "Show all contacts information [Show]\n" \
           "Stop bot [Goodbye, close or exit]\n"
