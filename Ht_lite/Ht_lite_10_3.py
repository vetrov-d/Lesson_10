from Classes.neg_num_err import NegativeNumberError

def check_positive_number(number):
    
    if number < 0:
        raise NegativeNumberError(number)

test_number = int(input('Введите положительное число:'))
check_positive_number(test_number)
print(f'Введенное значение: {test_number}')