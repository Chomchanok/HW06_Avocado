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

## 2.1 Which region sold the smallest amount of avocado ?
min = sum_each_region.min() # find min value
small = sum_each_region['Total Volume'].idxmin() # find max index of max value
print(" The region which sold the smallest amount of avocado is {} which is {}$".format(small,min.values))

## 2.2 In this region, where the biggest lot of sold avocado came from (4046, 4225, 4770) ?
min_lot_4046 = lot_4046.min()# find min value of PLU 4046 
min_lot_4225 = lot_4225.min()# find min value of PLU 4225
min_lot_4770 = lot_4770.min()# find min value of PLU 4770

combinemin = min_lot_4046.append([min_lot_4225,min_lot_4770]) # To combine min values from each PLUs
print("The biggest lot of sold avocado came from : ",combinemin.idxmax())

## 3. Which region sold the highest price of avocado in average ?
region_avg_price = df.groupby(['region'],sort=False)[['AveragePrice']].mean() # group by each region to calculate average price of avocado 
highest_avg_price = region_avg_price['AveragePrice'].idxmax() # find max indext of highest price 
print("The region which sold the highest price of avocado in average is : ",highest_avg_price )

## 4. Find the total amount of income (Avg_Price*Total_Volume) of each region.
merge = pd.DataFrame({'Total Volume':sum_each_region['Total Volume'],  # combine 2 series of total volume and average price by each region
                      'AveragePrice':region_avg_price['AveragePrice']})
merge['Total amount of income'] = merge['AveragePrice']*merge['Total Volume'] # add Total amount of income columns into dataframe 
print(merge)