import pandas as pd
import matplotlib.pyplot as plt
from random import choice, randint

initial_alphabet = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя (),'

steps = randint(10000, 30000)

input_string = ''

for _ in range(0, steps):
    input_string += choice(initial_alphabet)

stat_dict = {}

for key in input_string:
    if key != ' ':
        if key.lower() not in stat_dict.keys():
            stat_dict[key.lower()] = 1
        else:
            stat_dict[key.lower()] += 1

data_frame = pd.DataFrame(list(stat_dict.items()), columns=['Key', 'Value'])

sorted_df = data_frame.sort_values('Value', ascending=False)

top = sorted_df.head(10)

plt.bar(top['Key'], top['Value'])
plt.show()