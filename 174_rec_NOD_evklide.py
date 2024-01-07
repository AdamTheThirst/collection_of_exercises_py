def nod(a, b):
    if a < b:
        a, b = b, a

    c = a % b

    if c == 0:
        return b
    else:
        return nod(b, c)

print('Этот скрипт помогает найти НОД для двух целых чисел')
a = input('Введите первое целое число: ')
b = input('Введите второе целое число: ')

print(f'НОД для {a} и {b}: {nod(int(a), int(b))}')