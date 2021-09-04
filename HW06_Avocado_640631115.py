import pandas as pd 
import numpy as np
df = pd.read_csv("avocado.csv")
df.head()

## 1.1 Which region sold the largest amount of avocado ?
sum_each_region = df.groupby(['region'],sort=False)[['Total Volume']].sum() # group by each region to calculate total amount of avocado
max = sum_each_region.max() # find max value
large = sum_each_region['Total Volume'].idxmax() # find max index of max value
print(" The region which sold the largest amount of avocado is {} which is {}$".format(large,max.values))


## 1.2 In this region, where the biggest lot of sold avocado came from (4046, 4225, 4770) ?
lot_4046 = df.groupby(['region'],sort=False)[['4046']].sum() 
lot_4225 = df.groupby(['region'],sort=False)[['4225']].sum()
lot_4770 = df.groupby(['region'],sort=False)[['4770']].sum() 

max_lot_4046 = lot_4046.max()
max_lot_4225 = lot_4225.max()
max_lot_4770 = lot_4770.max()

combinemax = max_lot_4046.append([max_lot_4225,max_lot_4770])
print("The biggest lot of sold avocado came from : ",combine.idxmax())

