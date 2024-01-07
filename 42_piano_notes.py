''' Вернуть частоту ноты фортепиано: от C0 до C8 '''

# Даны частоты для октавы C4
table_of_base_frequency = {'C': 261.63,
                            'D': 293.66,
                            'E': 329.63,
                            'F': 349.23,
                            'G': 392.0,
                            'A': 440.0,
                            'B': 493.88,}

table_of_dividers = {0: 0.0625,
                     1: 0.125,
                     2: 0.25,
                     3: 0.5,
                     4: 1,
                     5: 2,
                     6: 4,
                     7: 8,
                     8: 16
}

next = False


def check_note(note):
    if len(note) != 2:
        return False
    if note[0] not in table_of_base_frequency.keys():
        return False
    if int(note[1]) not in range(0, 9):
        return False
    else:
        return True

print('Введите название ноты (Cx, Dx, Ex, Fx, Gx, Ax, Bx -- x:0-8)')

while not next:
    note = input('Ваша нота: ')
    next = check_note(note)

    if not next:
        print('Введены некорректные данные (образец: C4), попробуйте ещё раз\n')
    else:
        base_note_freq = float(table_of_base_frequency[note[0]])
        note_freq = base_note_freq * table_of_dividers[int(note[1])]
        print(f'Частота звука ноты {note} — {note_freq}Hz')
