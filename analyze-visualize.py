import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load the data files:
df_low = pd.read_csv('data/low.csv')
df_medium = pd.read_csv('data/medium.csv')
df_moderate = pd.read_csv('data/moderate.csv')
df_high = pd.read_csv('data/high.csv')


# histogram for proportion women/men (literacy and mean years in school):

literacy = (df_low.lit_female[36]/df_low.lit_male[36],df_medium.lit_female[36]/df_medium.lit_male[36],df_moderate.lit_female[36]/df_moderate.lit_male[36],df_high.lit_female[36]/df_high.lit_male[36])
school = (df_low.sc_female[36]/df_low.sc_male[36],df_medium.sc_female[36]/df_medium.sc_male[36],df_moderate.sc_female[36]/df_moderate.sc_male[36],df_high.sc_female[36]/df_high.sc_male[36])

n = 4          # 4 groups
ind = np.arange(n)
width = 0.2

plt.subplots()
plt.bar(ind - width/2, literacy, width, color='cornflowerblue', label='literacy rates', linewidth=0,align='center')
plt.bar(ind + width/2, school, width, color='yellowgreen', label='mean years in school',linewidth=0,align='center')

plt.axhline(0.5,color='gray',ls='--')
plt.axhline(1.0,color='gray',ls='--')
plt.title('proportion of women compared to men for \n literacy rates and mean years in school (2011)')
plt.ylabel('proportion women/men')
plt.xticks(ind, ('low','medium','moderate','high'))
plt.ylim(0,1.1)
plt.legend(loc='upper left')
plt.savefig('proportion_hist.png')
plt.close()


# computing trends:

def compute_trend(df,var):
    df_new = df[['years',var]]
    df_new.dropna(inplace=True)    # missing values need to be dropped to compute the trends
    years = df_new.years
    trend = np.polyfit(years,df_new[var],1)
    return years, trend


# plotting literacy rates for males:

low_years,low_trend = compute_trend(df_low,'lit_male')
medium_years,medium_trend = compute_trend(df_medium,'lit_male')
moderate_years,moderate_trend = compute_trend(df_moderate,'lit_male')
high_years,high_trend = compute_trend(df_high,'lit_male')

plt.subplots()

plt.scatter(df_low.years, df_low.lit_male, color = 'blue', label='_nolegend_')
plt.plot(low_years,low_trend[1]+low_trend[0]*low_years, color = 'blue', label='low')

plt.scatter(df_medium.years, df_medium.lit_male, color = "red", label='_nolegend_')
plt.plot(medium_years,medium_trend[1]+medium_trend[0]*medium_years, color = 'red', label='medium')

plt.scatter(df_moderate.years, df_moderate.lit_male, color = "green", label='_nolegend_')
plt.plot(moderate_years,moderate_trend[1]+moderate_trend[0]*moderate_years, color = 'green', label='moderate')

plt.scatter(df_high.years, df_high.lit_male, color = "orange", label='_nolegend_')
plt.plot(high_years,high_trend[1]+high_trend[0]*high_years, color = 'orange', label='high')

plt.title('literacy rates for men')
plt.xlabel('years')
plt.ylabel('literacy rate [%]')
plt.xlim(1970,2015)
plt.ylim(0,101)
plt.legend(loc='lower right')
plt.savefig('literacy_male_trend.png')
plt.close()


# plotting literacy rates for females:

low_years,low_trend = compute_trend(df_low,'lit_female')
medium_years,medium_trend = compute_trend(df_medium,'lit_female')
moderate_years,moderate_trend = compute_trend(df_moderate,'lit_female')
high_years,high_trend = compute_trend(df_high,'lit_female')

plt.subplots()

plt.scatter(df_low.years, df_low.lit_female, color = 'blue', label='_nolegend_')
plt.plot(low_years,low_trend[1]+low_trend[0]*low_years, color = 'blue', label='low')

plt.scatter(df_medium.years, df_medium.lit_female, color = "red", label='_nolegend_')
plt.plot(medium_years,medium_trend[1]+medium_trend[0]*medium_years, color = 'red', label='medium')

plt.scatter(df_moderate.years, df_moderate.lit_female, color = "green", label='_nolegend_')
plt.plot(moderate_years,moderate_trend[1]+moderate_trend[0]*moderate_years, color = 'green', label='moderate')

plt.scatter(df_high.years, df_high.lit_female, color = "orange", label='_nolegend_')
plt.plot(high_years,high_trend[1]+high_trend[0]*high_years, color = 'orange', label='high')

plt.title('literacy rates for women')
plt.xlabel('years')
plt.ylabel('literacy rate [%]')
plt.xlim(1970,2015)
plt.ylim(0,101)
plt.legend(loc='lower right')
plt.savefig('literacy_female_trend.png')
plt.close()


# plotting all trendlines together:

plt.subplots()

low_years,low_trend = compute_trend(df_low,'lit_male')
medium_years,medium_trend = compute_trend(df_medium,'lit_male')
moderate_years,moderate_trend = compute_trend(df_moderate,'lit_male')
high_years,high_trend = compute_trend(df_high,'lit_male')

plt.plot(low_years,low_trend[1]+low_trend[0]*low_years, color = 'blue', label='low')
plt.plot(medium_years,medium_trend[1]+medium_trend[0]*medium_years, color = 'red', label='medium')
plt.plot(moderate_years,moderate_trend[1]+moderate_trend[0]*moderate_years, color = 'green', label='moderate')
plt.plot(high_years,high_trend[1]+high_trend[0]*high_years, color = 'orange', label='high')

low_years,low_trend = compute_trend(df_low,'lit_female')
medium_years,medium_trend = compute_trend(df_medium,'lit_female')
moderate_years,moderate_trend = compute_trend(df_moderate,'lit_female')
high_years,high_trend = compute_trend(df_high,'lit_female')

plt.plot(low_years,low_trend[1]+low_trend[0]*low_years, color = 'blue', label='_nolegend_', ls='--')
plt.plot(medium_years,medium_trend[1]+medium_trend[0]*medium_years, color = 'red', label='_nolegend_', ls='--')
plt.plot(moderate_years,moderate_trend[1]+moderate_trend[0]*moderate_years, color = 'green', label='_nolegend_', ls='--')
plt.plot(high_years,high_trend[1]+high_trend[0]*high_years, color = 'orange', label='_nolegend_', ls='--')

plt.title('trends of literacy rates for men and women')
plt.xlabel('years')
plt.ylabel('literacy rate [%]')
plt.ylim(0,101)
plt.xlim(1970,2015)
plt.legend(loc='lower right')
plt.savefig('literacy_male-female_trend.png')
plt.close()


# plotting mean years in school:

plt.subplots()

plt.plot(df_low.years, df_low.sc_male, color = 'blue', label='low')
plt.plot(df_medium.years, df_medium.sc_male, color = "red", label='medium')
plt.plot(df_moderate.years, df_moderate.sc_male, color = "green", label='moderate')
plt.plot(df_high.years, df_high.sc_male, color = "orange", label='high')

plt.plot(df_low.years, df_low.sc_female, color = 'blue', label='_nolegend_', ls='--')
plt.plot(df_medium.years, df_medium.sc_female, color = "red", label='_nolegend_', ls='--')
plt.plot(df_moderate.years, df_moderate.sc_female, color = "green", label='_nolegend_', ls='--')
plt.plot(df_high.years, df_high.sc_female, color = "orange", label='_nolegend_', ls='--')

plt.title('mean time in school for men and women')
plt.xlabel('years')
plt.ylabel('years in school')
plt.xlim(1970,2015)
plt.ylim(0,14)
plt.legend(loc='upper left')
plt.savefig('school_trend.png')
plt.close()


