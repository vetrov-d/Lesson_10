def convert_to_int(value):
    error = 0
    try:
        number = int(value)
        if number < 0:
            raise TypeError('Введено отрицательное число')
    except ValueError:
        print(f'Невозможно преобразовать {value} в число')
        error += 1
    except BaseException as be:
        print(f'Тип ошибки {type(be).__name__}')
        print(f'Сообщение об ошибке {be}')
        error += 1
    else:
        print(f'Результат преобразования: {number}')
    finally:
        if error == 0:
            print(f'Преобразование данных {value} корректно завершено\n')
        else:
            print(f'Преобразование данных {value} не выполнено. Возникла ошибка\n')
        
str_for_convert = ''
while str_for_convert != 'q':
    str_for_convert = input('Введите строку для преобразования в число:')
    number = convert_to_int(str_for_convert)
    
            
        
           