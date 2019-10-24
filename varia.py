import pandas as pd
import matplotlib.pyplot as plt

# Reading file
wdiw_data = pd.read_excel('WDIW dataset.xlsx')
wdiw_meta=pd.read_excel('WDI_Metadata.xlsx')

#Filtering out everything except the 'Hot Rod' values.
wdiw_hr = wdiw_data.loc[wdiw_data['Cool Name'] == 'Hot Rod']

#Calculating missing values
missing_values = wdiw_hr.isnull().sum().sum()
print(missing_values)

#All the medians
wdiw_median = wdiw_hr.iloc[:, 4:].median()

#All the means
wdiw_mean = wdiw_hr.iloc[:, 4:].mean().round(2)

#All descriptive data

col=wdiw_hr.columns
info=wdiw_hr.info
desc=wdiw_hr.describe()

count=11
#Look for our variables 

print(wdiw_hr['Access to electricity (% of population)'].describe())
print(wdiw_hr['Access to electricity, rural (% of rural population)'].describe())
print(wdiw_hr['Access to electricity, urban (% of urban population)'].describe())
#Missing values in agriculture
print(wdiw_hr["Agriculture, forestry, and fishing, value added (% of GDP)"].describe())
#Missing values
print(wdiw_hr['Armed forces personnel (% of total labor force)'].describe())
#Missing values
print(wdiw_hr['Employment in agriculture (% of total employment) (modeled ILO estimate)'].describe())
#Missing values
print(wdiw_hr['Employment in industry (% of total employment) (modeled ILO estimate)'].describe())
#Missing values, wrong statistics
print(wdiw_hr['Employment in services (% of total employment) (modeled ILO estimate)'].describe())
#Missing values
print(wdiw_hr['GDP (current US$)'].describe())
#Missing values
print(wdiw_hr['GDP growth (annual %)'].describe())
#Missing values
print(wdiw_hr["Industry (including construction), value added (% of GDP)"].describe())
#Missing values
print(wdiw_hr['Merchandise trade (% of GDP)'].describe())
#Missing values
print(wdiw_hr['Military expenditure (% of GDP)'].describe())
print(wdiw_hr['Population density (people per sq. km of land area)'].describe())
#Missing values
print(wdiw_hr['Population in the largest city (% of urban population)'].describe())
print(wdiw_hr['Population living in slums (% of urban population)'].describe())
#Missing values
print(wdiw_hr['Rural population (% of total population)'].describe())
#Missing values
print(wdiw_hr["Services, value added (% of GDP)"].describe())
#missing values, we can added it I think surface area hasn't changed, worng data
print(wdiw_hr['Surface area (sq. km)'].describe())
#Missing values
print(wdiw_hr['Tax revenue (% of GDP)'].describe())
print(wdiw_hr['Urban population (% of total population)'].describe())
print(wdiw_hr['Urban population growth (annual %)'].describe())

#if wdiw_meta['Indicator Name']=='Urban population growth (annual %)':
     # print(wdiw_meta['Long definition'])
