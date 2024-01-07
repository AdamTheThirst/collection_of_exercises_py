'''Проверяет, введён ли полиндром'''

inp_str = input('Пожалуйста, введите строку: ')
inp_str = inp_str.replace(' ', '')
rev_str = ''.join(reversed(inp_str))

if inp_str.lower() == rev_str.lower():
    nop = ''
else:
    nop = 'не '

print(f'Ваша строка — {nop}полиндром')