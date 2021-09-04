import pandas as pd 
import numpy as np
df = pd.read_csv("avocado.csv")
df.head()

## 1.1 Which region sold the largest amount of avocado ?
sum_each_region = df.groupby(['region'],sort=False)[['Total Volume']].sum()
max = sum_each_region.max()
large = sum_each_region['Total Volume'].idxmax()
print(" The region which sold the largest amount of avocado is {} which is {}$".format(large,max.values))


