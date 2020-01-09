import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load the data files:
df_mean_lit = pd.read_csv('data/mean_literacy_total.csv')
df_lit_male = pd.read_csv('data/literacy_male.csv')
df_lit_female = pd.read_csv('data/literacy_female.csv')
df_sc_male = pd.read_csv('data/school_male.csv')
df_sc_female = pd.read_csv('data/school_female.csv')

# general exploration of df_lit_male:
print(df_lit_male.head())
shape = df_lit_male.shape
ncountries = shape[0]
nyears = shape[1]
print('{} countries in dataset'.format(ncountries))
print('{} years in dataset'.format(nyears))
missperrow = df_lit_male.isnull().sum(axis=1)
mindatarow = nyears - max(missperrow)
print('every country has at least {} years with data'.format(mindatarow))
datapercol = df_lit_male.count()
print('non-missing values per year:')
print(datapercol)

# general exploration of df_lit_female:
print(df_lit_female.head())
shape = df_lit_female.shape
ncountries = shape[0]
nyears = shape[1]
print('{} countries in dataset'.format(ncountries))
print('{} years in dataset'.format(nyears))
missperrow = df_lit_female.isnull().sum(axis=1)
mindatarow = nyears - max(missperrow)
print('every country has at least {} years with data'.format(mindatarow))
datapercol = df_lit_female.count()
print('non-missing values per year:')
print(datapercol)

# general exploration of df_sc_male:
print(df_sc_male.head())
shape = df_sc_male.shape
ncountries = shape[0]
nyears = shape[1]
print('{} countries in dataset'.format(ncountries))
print('{} years in dataset'.format(nyears))
missperrow = df_sc_male.isnull().sum(axis=1)
mindatarow = nyears - max(missperrow)
print('every country has at least {} years with data'.format(mindatarow))
datapercol = df_sc_male.count()
print('non-missing values per year:')
print(datapercol)

# general exploration of df_sc_female:
print(df_sc_female.head())
shape = df_sc_female.shape
ncountries = shape[0]
nyears = shape[1]
print('{} countries in dataset'.format(ncountries))
print('{} years in dataset'.format(nyears))
missperrow = df_sc_female.isnull().sum(axis=1)
mindatarow = nyears - max(missperrow)
print('every country has at least {} years with data'.format(mindatarow))
datapercol = df_sc_female.count()
print('non-missing values per year:')
print(datapercol)

# making sure all dataframes contain the same countries as in df_mean_lit (and dropping all extra countries):
countries = list(df_mean_lit['geo'])
df_lit_male = df_lit_male.query('geo in @countries')
df_sc_male = df_sc_male.query('geo in @countries')
df_lit_female = df_lit_female.query('geo in @countries')
df_sc_female = df_sc_female.query('geo in @countries')

print('{} countries in dataset df_mean_lit'.format(df_mean_lit.shape[0]))
print('{} countries in dataset df_lit_male'.format(df_lit_male.shape[0]))
print('{} countries in dataset df_lit_female'.format(df_lit_female.shape[0]))
print('{} countries in dataset df_sc_male'.format(df_sc_male.shape[0]))
print('{} countries in dataset df_sc_female'.format(df_sc_female.shape[0]))

# deviding the countries into 4 groups based on the total literacy:
descr = df_mean_lit['mean'].describe()
print(descr)
l_min = descr['min']
l_q25 = descr['25%']
l_q50 = descr['50%']
l_q75 = descr['75%']
l_max = descr['max']
bin_edges = [l_min, l_q25, l_q50, l_q75, l_max]
bin_names = ['low','medium','moderate','high']
df_mean_lit['level'] = pd.cut(df_mean_lit['mean'], bin_edges, labels=bin_names)
print(df_mean_lit.head())

c_low = list(df_mean_lit.query('level == "low"')['geo'])
c_medium = list(df_mean_lit.query('level == "medium"')['geo'])
c_moderate = list(df_mean_lit.query('level == "moderate"')['geo'])
c_high = list(df_mean_lit.query('level == "high"')['geo'])
print('countries with "low"-literacy rates ({} to {}):'.format(l_min,l_q25))
print(c_low)
print('countries with "medium"-literacy rates ({} to {}):'.format(l_q25,l_q50))
print(c_medium)
print('countries with "moderate"-literacy rates ({} to {}):'.format(l_q50,l_q75))
print(c_moderate)
print('countries with "high"-literacy rates ({} to {}):'.format(l_q75,l_max))
print(c_high)

# creating 4 new data frames combining info on male/female literacy and school years:
df_low = pd.DataFrame()
df_low['lit_male'] = df_lit_male.query('geo in @c_low').mean()
df_low['lit_female'] = df_lit_female.query('geo in @c_low').mean()
df_low['sc_male'] = df_sc_male.query('geo in @c_low').mean()
df_low['sc_female'] = df_sc_female.query('geo in @c_low').mean()
df_low.index.name = 'years'
print(df_low.head())

df_medium = pd.DataFrame()
df_medium['lit_male'] = df_lit_male.query('geo in @c_medium').mean()
df_medium['lit_female'] = df_lit_female.query('geo in @c_medium').mean()
df_medium['sc_male'] = df_sc_male.query('geo in @c_medium').mean()
df_medium['sc_female'] = df_sc_female.query('geo in @c_medium').mean()
df_medium.index.name = 'years'
print(df_medium.head())

df_moderate = pd.DataFrame()
df_moderate['lit_male'] = df_lit_male.query('geo in @c_moderate').mean()
df_moderate['lit_female'] = df_lit_female.query('geo in @c_moderate').mean()
df_moderate['sc_male'] = df_sc_male.query('geo in @c_moderate').mean()
df_moderate['sc_female'] = df_sc_female.query('geo in @c_moderate').mean()
df_moderate.index.name = 'years'
print(df_moderate.head())

df_high = pd.DataFrame()
df_high['lit_male'] = df_lit_male.query('geo in @c_high').mean()
df_high['lit_female'] = df_lit_female.query('geo in @c_high').mean()
df_high['sc_male'] = df_sc_male.query('geo in @c_high').mean()
df_high['sc_female'] = df_sc_female.query('geo in @c_high').mean()
df_high.index.name = 'years'
print(df_high.head())

# write data to new files:
df_low.to_csv('data/low.csv', index=True)
df_medium.to_csv('data/medium.csv', index=True)
df_moderate.to_csv('data/moderate.csv', index=True)
df_high.to_csv('data/high.csv', index=True)

