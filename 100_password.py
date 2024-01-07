'''Генерация случайного пароля из ASCII
и проверка его на надёжность.
Условия: минимум 1 цифра, одна буква в верхнем регистре, 1 буква в нижнем регистре, длина не менее 8 символов'''

from random import randint

MIN = 5
MAX = 11
START = 33
END = 126

def generate_password():
    pass_len = randint(MIN, MAX)
    my_pass = ''
    for _ in range(0, pass_len):
        my_pass = my_pass + chr(randint(START, END))
    return my_pass

def is_password_strong(my_pass):
    alphabet_upper_case = [41, 90]
    alphabet_lower_case = [97, 122]
    numbers = [48, 57]
    strong = [0,0,0]
    if len(my_pass) > 7:
        for symbol in my_pass:
            if ord(symbol) in range(alphabet_upper_case[0], alphabet_upper_case[1]):
                if strong[0] == 0:
                    strong[0] = 1
            if ord(symbol) in range(alphabet_lower_case[0], alphabet_lower_case[1]):
                if strong[1] == 0:
                    strong[1] = 1
            if ord(symbol) in range(numbers[0], numbers[1]):
                if strong[2] == 0:
                    strong[2] = 1

    if strong[0]+strong[1]+strong[2] == 3:
        return True
    else:
        return False

if __name__ == '__main__':
    my_pass = generate_password()
    is_pass_strong = is_password_strong(my_pass)
    nop = ''
    if not is_pass_strong:
        nop = 'не '

    print(f'Сгенерированный пароль {my_pass} {nop}надёжен')