import re

string = "Всем привет! Меня зовут Алексей. Мой email: alexVB@gmail.com. " \
         "Привет, Алексей! Меня зовут Марина, моя почта: Marina@mail.ru"


def find_email(str):
    email = re.findall(r"\w+@[a-zA-Z]+?\.[a-zA-Z]{2,6}", str)
    return email


print(find_email(string))