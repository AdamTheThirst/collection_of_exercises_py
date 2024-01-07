def decimal_to_binary(num, my_str=''):
    if num == 0:
        return my_str
    else:
        c = num % 2
        my_str = str(c) + my_str
        c = num // 2
        return decimal_to_binary(c, my_str)

my_num = input('Введите целое число для последующего перевода в двоичное: ')
my_num = int(my_num)
print(decimal_to_binary(my_num))