def is_polindrome(input_str):
    if len(input_str) <= 1:
        return True
    elif input_str[0].lower() == input_str[-1].lower():
        return is_polindrome(input_str[1:-2])
    else:
        return False



input_str = input('Введите строку: ')
input_str = input_str.replace(' ', '')
print(is_polindrome(input_str))
