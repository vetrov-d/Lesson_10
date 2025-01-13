class UserAlreadyExistsError(Exception):
        def __init__(self, username, message_error = "Пользователь с таким именем уже существует"):
            self.username = username
            self.message_error = message_error
            super().__init__(self.message_error)
    
        def __str__(self):
            return (f'{self.message_error}: {self.username}')   