# Базовый класс User и производные классы для различных типов пользователей
from classes.user_exist import UserAlreadyExistsError
from classes.user_not_found import UserNotFoundError


class User:
    """
    Базовый класс, представляющий пользователя.
    """
    #users = {} #Словарь для хранения всех пользователей
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age
        
    def __str__(self):
        return f'Имя={self.username}, почта={self.email}, возраст={self.age}'
       
class UserManager:
    def __init__(self, users):
        self.users = users
   
    def add_user(self, user: User):      
        if user.username in self.users.keys():
            print(f'Пользователь с именем {user.username} уже есть')
            raise UserAlreadyExistsError(user.username)
        else:
            self.users[user.username] = user
            print(f"Пользователь {user.username} зарегистрирован")
        return self.users.items
    
    def remove_user(self, username: str):
        if username in self.users.keys():
            deleted_user = self.users.pop(username)
            return deleted_user
        else:
            print(f'Пользователя с именем {username} не найдено')
            raise UserNotFoundError(username)
        
    def find_user(self, username: str):
        if username in self.users.keys():
            return self.users[username]
        else:
            print(f'Пользователя с именем {username} не найдено')
            raise UserNotFoundError(username) 