# Урок 15. Семинар. Построение графиков
# | Задание 44 |
# | --- |
# | В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
# data.head() |

import pandas as pd
import random

# Генерация исходных данных
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Преобразование в one-hot вид
one_hot = pd.DataFrame(
    {category: (data['whoAmI'] == category).astype(int) for category in data['whoAmI'].unique()}
)

# Объединяем оригинальный DataFrame и one-hot представление
result = pd.concat([data, one_hot], axis=1)

print(result)




