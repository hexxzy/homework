import re

class Phone:
    def __init__(self):
        self.country
        self.city
        self.station
        self.number
    def get_phone(self):
        str = input("Enter phone number: ")
        result = re.compile(r"((\+[0-9][ -])?)\(?(\d{3})\)?[ -]?(\d{3})[ -]?(\d{4})", str)
        return result

my_phone = Phone()
my_phone.set_attrs()
my_phone.print_phone()
#не выполнено