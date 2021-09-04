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
lot_4046 = df.groupby(['region'],sort=False)[['4046']].sum() # group by region to calculate total amount of avocado in PLU 4046 
lot_4225 = df.groupby(['region'],sort=False)[['4225']].sum() # group by region to calculate total amount of avocado in PLU 4225
lot_4770 = df.groupby(['region'],sort=False)[['4770']].sum() # group by region to calculate total amount of avocado in PLU 4770

max_lot_4046 = lot_4046.max() # find max value of PLU 4046 
max_lot_4225 = lot_4225.max() # find max value of PLU 4225
max_lot_4770 = lot_4770.max() # find max value of PLU 4770

combinemax = max_lot_4046.append([max_lot_4225,max_lot_4770]) # To combine max values from each PLUs
print("The biggest lot of sold avocado came from : ",combinemax.idxmax()) 

