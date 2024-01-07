from random import randint

value = randint(30, 100)

def summ(value):
    if value != 0:
        return value + summ(value-1)
    else:
        return 0

print(f'Сумма всех целых чисел до {value} включительно - {summ(value)}')





def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

n = randint(5, 30)

print(f'Число фибоаччи для {n} - {fibo(n)}')