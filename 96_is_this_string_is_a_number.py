'''
Получить строку и проверить,
является ли она числом
'''

my_str = input('Введите строку: ')
my_str = my_str.lstrip().rstrip()

def is_it_number(my_str):
    sign = ['+', '-']
    sign_float = ['.', '.']
    digits = '1234567890'
    is_float = False
    if my_str[0] in sign:
        start = 1
    else:
        start = 0

    for i in range(start, len(my_str)):
        if my_str[i] not in digits:
            if i > 0 and my_str[i] in sign_float:
                if  is_float == True:
                    return False
                else:
                    is_float = True
            else:
                return False

    return True

if is_it_number(my_str):
    ans = ''
else:
    ans = ' не'

print(f'Ваша строка{ans} является числом')