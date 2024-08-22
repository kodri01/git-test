from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, username, email):
        self.username = username
        self.email = email

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

    def display_info(self):
        print(f'Username : {self.username}')
        print(f'Email : {self.email}')

class Admin(User):
    def __init__(self, username, email, level):
        super().__init__(username, email)
        self.level = level
    
    def login(self):
        print('Loggin in as Admin')

    def logout(self):
        print('Loggin out....')
    
    def display_info(self):
        super().display_info()
        print(f'Admin Level : {self.level}')

class Reguler(User):
    def login(self):
        print('Loggin in as Reguler User')
    def logout(self):
        print('Loggin out....')
    
    def display_info(self):
        super().display_info()

def manage_user(user):
    user.login()
    user.display_info()
    user.logout()

admin = Admin('adminUser1', 'admin@gmail.com', 2)
user = Reguler('userReguler', 'userReguler@gmail.com')

print('Admin User :')
manage_user(admin)
print('')
print('Reguler User :')
manage_user(user)
    

        