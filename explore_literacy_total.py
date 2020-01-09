import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load the data on total literacy:
df = pd.read_csv('data/literacy_total.csv')
print(df.head())

# the shape gives the number of countries and years available:
shape = df.shape
ncountries = shape[0]
nyears = shape[1]
print('{} countries in dataset'.format(ncountries))
print('{} years in dataset'.format(nyears))

# number of missing values per country:
missperrow = df.isnull().sum(axis=1)
mindatarow = nyears - max(missperrow)
print('every country has at least {} years with data'.format(mindatarow))

# number of missing values per year
datapercol = df.count()
print('non-missing values per year:')
print(datapercol)

# looking only at the last 12 years
cols = ['geo']
cols += list(range(2000,2012))
cols = list(map(str,cols))
df = df[cols]
print(df.head())

# see if there is data for all countries:
missperrow = df.isnull().sum(axis=1)
mindatarow = 12 - max(missperrow)
print('every country has at least {} years with data'.format(mindatarow))

# how many rows do not contain data at all:
cols = list(range(2000,2012))
cols = list(map(str,cols))
nrowdrop = df.shape[0] - df[cols].dropna(axis=0,how='all').shape[0]
print('{} countries do not have any data in the last 12 years'.format(nrowdrop))

# drop rows without data (besides country info):
df.dropna(axis=0,thresh=2,inplace=True)
print(df.shape)

# find the mean literacy rate for each country in the last 12 years of data:
means = df.mean(axis=1)
df['mean'] = means
df_mean = df[['geo','mean']]
print(df_mean.head())

# write mean data to new file:
df_mean.to_csv('data/mean_literacy_total.csv', index=False)

