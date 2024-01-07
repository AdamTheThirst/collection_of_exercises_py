''' Понять, какой треугольник: равнобедренный, равносторонний или разносторонний '''
import re

def is_numeric(number):
    if number.isnumeric():
        return int(number)
    else:
        is_float_regex = re.compile(r'(\d+)(.|,)(\d+)')
        num = is_float_regex.search(number)
        if num is not None:
            return float(number)
        else:
            return False

print('Введите значния длин сторон треугольника')
triangle = list()
while len(triangle)<3:
    a = input('Введите значение: ')
    if is_numeric(a) is not False:
        triangle.append(a)
    else:
        print('Значение должно быть числом')

triangle_set = set(triangle)

triangle_types = {1: 'Равносторонний треугольник',
                  2: 'Равнобедренный треугольник',
                  3: 'Разносторонний треугольник'}

print(triangle_types[len(triangle_set)])

