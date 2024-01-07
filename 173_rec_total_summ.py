def summ():
    a = input('Введите целое положительно число: ')
    if a == '':
        return 0
    else:
        return int(a) + summ()
total = summ()
print(f'Сумма всех введённых чисел: {total}')
