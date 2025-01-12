class NegativeNumberError(Exception):
    def __init__(self, number, message_error = "Введено отрицательное значение"):
        self.number = number
        self.message_error = message_error
        super().__init__(self.message_error)
    
    def __str__(self):
        return (f'{self.message_error}: {self.number}')   