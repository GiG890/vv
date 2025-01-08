class UserAccount:
    def __init__(self, username, email, password):
        self.username=username
        self.email=email
        self.__password=password

    def set_password(self, new_password):
        self.__password=new_password

    def check_password(self, password):
        return True if self.__password==password else False

a=UserAccount("Bobik", "Bobik@.com", "12345qwerty")
a.set_password("12345qwertrrrrr")
print(a.check_password("12345qwerty"))
