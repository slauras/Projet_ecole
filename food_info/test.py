import pandas as pd
import numpy as np
import functools

food_info = pd.read_csv("food_info.csv")
num_row = food_info.shape[0]

gcol = []
for col in list(food_info.columns):
    if col.endswith('(g)'):
        gcol.append(col)

gcol2 = list(filter(
    (lambda str:str.endswith('(g)')),
    list(food_info.columns)))

print(gcol)

print(gcol2)

