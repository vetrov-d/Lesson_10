def validate_user_input(data):
    if type(data) != dict:
        raise TypeError('Входные данные не являются словарем\n')
    else:
        if ('name' in data) and ('age' in data):
            if (type(data['age']) != str) and (type(data['name']) == str):
                if (data['age'] > 0):
                    print(f'Данные пользователя: имя: {data['name']}, возраст: {data['age']}')
                    print()
        if  'name' in data:
            if  type(data['name']) != str:
                raise ValueError(f'Тип {data['name']} не является строковым\n')
        else:
            raise ValueError('Во входных данных нет ключа "name"\n')
        if  'age' in data:
            if  type(data['age']) == str:
                raise ValueError(f'Значение возраста {data['age']} не является числом\n')
            else:
                if  data['age'] <= 0:
                    raise ValueError('Значение возраста отрицательное\n') 
        else:
            raise ValueError('Во входных данных нет ключа "age"\n')
     
right_data = {'name': 'Alice', 'age': 30}
wrong_data_1 = {'number': 'Alice', 'age': 30}
wrong_data_2 = {'name': 125, 'age': 30}
wrong_data_3 = {'name': 'Alice', 'years': 30}
wrong_data_4 = {'name': 'Alice', 'age': -97}
wrong_data_5 = {'name': 'Alice', 'age': 'abc'}
wrong_data_6 = 'Входные данные'
validate_user_input(wrong_data_6)
