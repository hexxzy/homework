import hashlib
from t6 import checker


class User:
    def __init__(self):
        self.get_login()
        self.get_password()

    def get_login(self):
        res = checker()
        if res != Exception:
            self.login = res
            return
        return self.get_login()

    def get_password(self):
        pasw = input("password: ")
        self.get_hash(pasw)

    def get_hash(self, str):
        self.password = hashlib.md5(str.encode("utf8"))


User_1 = User()
print(User_1.__dict__)