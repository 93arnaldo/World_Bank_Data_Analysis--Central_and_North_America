# Hot-Rod-Analysis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Reading file
wdiw_data = pd.read_excel('WDIW_Dataset.xlsx')

#Filtering out everything except the 'Hot Rod' values.
wdiw_hr = wdiw_data.loc[wdiw_data['Cool Name'] == 'Hot Rod']

#Calculating missing values
missing_values = wdiw_hr.isnull().sum().sum()

#All the medians
wdiw_median = wdiw_hr.iloc[:, 4:].median()
