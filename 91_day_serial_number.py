'''
Получить у пользователя дату,
вернуть порядковый номер дня в году
и порядковый номер дня, начиная от 0-го года
'''

import pyinputplus as pyip

def is_leap_year(year):
    if year % 4 == 0:
        if year < 399 or ((year % 100 == 0) and (year % 400 == 0)):
            return True
    else:
        return False

def max_days_in_mounth(mounth, year):
    if mounth == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    elif (mounth < 7 and mounth % 2 == 0) or (mounth > 7 and mounth % 2 != 0):
        return 30
    else:
        return 31

def day_serial_number(year, mounth, day):
    day_serial_number = 0
    if year > 0:
        for i in range(mounth-1):
            day_serial_number += max_days_in_mounth(mounth=i+1, year=year)
    return day_serial_number+day

def absolute_day_serial_number(year, mounth, day):
    absolute_day_serial_number = 0
    for i in range(year-1):
        if is_leap_year(i+1):
            absolute_day_serial_number += 366
        else:
            absolute_day_serial_number += 365

    return absolute_day_serial_number + day_serial_number(year, mounth, day)


year = pyip.inputInt('Введите год: ', greaterThan=-1)
mounth = pyip.inputInt('Введите месяц (1 - 12): ', min=1, max=12)
dmax = max_days_in_mounth(mounth=mounth, year=year)
day = pyip.inputInt(f'Введите день (1 - {dmax}): ', min=1, max=dmax)
print(f'Порядковый номер дня в году: {day_serial_number(year, mounth, day)}')
print(f'Порядковый номер дня в году, начиная с 0-го года: {absolute_day_serial_number(year, mounth, day)}')