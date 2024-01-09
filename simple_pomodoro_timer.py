#simple pomodoro timer

from time import sleep

WORK_TIME = 1 #min
REST_TIME = 10 #min


finish_flag = False
is_rest = False


def timer(min, is_rest):
    seconds = min * 60
    label = 'Work time: '
    if is_rest:
        label = 'Rest time: '

    while seconds >= 0:
        timer = divmod(seconds, 60)
        print(f"{label}{timer[0]:02d}:{timer[1]:02d}", end='')
        sleep(1)
        print('\r' + ' ' * 50, end='\r')
        seconds -= 1
    is_rest = not is_rest
    return is_rest


while not finish_flag:
    if not is_rest:
        timer(WORK_TIME, is_rest)
        is_rest = True
    else:
        timer(REST_TIME, is_rest)
        finish_flag = not finish_flag
