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

