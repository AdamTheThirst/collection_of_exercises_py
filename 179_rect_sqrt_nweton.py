# получить число для уточнения, когда выйти из цикла
c = 10
for _ in range(0,12):
    c = c/10

def nsqrt(x, guess=1):
    if guess == 1:
        return nsqrt(x, x/2)
    elif abs(x - guess*guess) > c:
        guess = 0.5 * (guess + x/guess)
        return nsqrt(x, guess)
    else:
        return guess

num = input('Введите число, из которого нужно извелчь квадратный корень: ')
print(f'Квадратный корень: {round(nsqrt(float(num)), 2)}')