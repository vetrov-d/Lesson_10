from classes.users import User, UserManager
from classes.user_exist import UserAlreadyExistsError
from classes.user_not_found import UserNotFoundError

# Создаем пользователей
customer1 = User(username="Dmitry", email="dvetrov@mege.ru", age = 37)
customer2 = User(username="Elizaweta", email="elizawetta@mail.ru", age = 35)
admin = User(username="root", email="root@mail.ru",  age = 47)
# Заполняем словарь с данными пользователей
users = {}
administration = UserManager(users)
administration.add_user(customer1)
administration.add_user(customer2)
administration.add_user(admin)
print(users.keys())
test_users = [customer1, customer2, admin]
# Добавляем пользователей которые зарегистрированы
for i in test_users:
    try:
        print(f'\nДобавляем пользователя {i.username}:')
        administration.add_user(i)
    except UserAlreadyExistsError:
        print(UserAlreadyExistsError(i))
# Удаляем пользователя
try:
    print(f'\nУдаляем пользователя: root:')
    print(f'Пользователь: {administration.remove_user('root')} удален')
except UserNotFoundError:
    print(UserNotFoundError('root'))
print(users.keys())
# Попытка удалить пользователяЮ который уже был удален
try:
    print(f'\nУдаляем пользователя: root:')
    print(f'Пользователь: {administration.remove_user('root')} удален')
except UserNotFoundError:
    print(UserNotFoundError('root'))
print(users.keys())
# Поиск пользователя
print(f'\nПоиск пользователя Elizaweta:')
print(f'\nНайден пользователь: {administration.find_user('Elizaweta')}')
print(f'\nПоиск пользователя root:')
print(f'\nНайден пользователь: {administration.find_user('root')}')