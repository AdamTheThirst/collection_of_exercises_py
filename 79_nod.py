''' Поиск наибольшего общего делителя НОД '''


print('Поиск НОД для двух чисел')

_next = False
while not _next:
    x = input('Введите первое целое число: ')
    y = input('Введите второе целое число: ')

    if not x.isnumeric() or not y.isnumeric():
        print('Введите числовое значение')
    elif int(x) == 0 or int(y) == 0:
        print('Число должно отличаться от 0')
    else:
        _next = True

x = int(x)
y = int(y)

if x < y:
    d = x
else:
    d = y

_next = False
while not _next:

    if x % d != 0 or y % d != 0:
        d = d - 1
    else:
        _next = True

print(f"НОД для {x} и {y}: {d}")