from collections import UserDict


class Field:
    def __init__(self, name):
        self.value = name


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, phone_number=""):
        super().__init__(self)
        self.value = phone_number


class Record:
    def __init__(self, name: Name, phones: list[Phone] = []) -> None:
        self.name = name
        self.phones = phones

    def add_number(self, number: Phone):
        self.phones.append(number)

    def del_number(self, number: Phone):
        for x in self.phones:
            if x.value == number.value:
                self.phones.remove(x)


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def delete_record(self, name: str):
        self.data.pop(name)



