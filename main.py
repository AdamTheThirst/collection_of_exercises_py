from random import randint

# arr = []
#
# for _ in range(0, 20):
#     arr.append(randint(1,100))
#
#
# def rec_summ(arr: list):
#     if len(arr) == 0:
#         return 0
#     else:
#         return arr[0] + rec_summ(arr[1:])
#
# print(rec_summ(arr))



from random import randint
intended_number = str(randint(100, 999))

CHECK_STRING = '1234567890'

MAX_ATTEMPTS = 10
true_number = 'BONGO'
true_position = 'BANGO'
true_ans = 'BINGO'

print('\n'
      f'Я загадаю трёхзначное число, Ваша задача с {MAX_ATTEMPTS} раз его угадать\n'
      f'Если в ответе будет правильная цифра на правильном месте, я скажу {true_number}\n'
      f'Если в ответе будет правильная цифра на правильном месте, я скажу {true_position}\n'
      f'Если ответ будет полностью правильным, я скажу {true_ans}\n'
      f'Начинаем {intended_number}')


def user_input(user_ans):
    if len(user_ans) != 3:
        print('Должно быть ровно три цифры!')
        return False
    for ch in user_ans:
        if ch not in CHECK_STRING:
            print('Должны быть только цыфры!')
            return False
    return True

def is_it_correct_answer(return_list:list):
    counter = 0

    for i in range(len(return_list)):
        if true_position == return_list[i]:
            counter += 1

    if counter == 3:
        return True
    else:
        return False

def check_number(user_ans):
    return_list = list()
    for ch in user_ans:
        if ch in intended_number:
            if user_ans.index(ch) == intended_number.index(ch):
                return_list.append(true_position)
            else:
                return_list.append(true_number)


    if is_it_correct_answer(return_list):
        return true_ans
    else:
        return return_list


for i in range(MAX_ATTEMPTS):
    exit_flag = False
    user_ans = ''
    while not exit_flag:
        user_ans = input(f'Попытка #{i}. Введите ответ: ')
        exit_flag = user_input(user_ans)
    res = check_number(user_ans)
    if res == true_ans:
        print('Вы правы!')
        break
    else:
        print(' '.join(res))

print(f'Правильный ответ: {intended_number}')