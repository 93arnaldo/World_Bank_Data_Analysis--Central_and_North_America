# Hot-Rod-Analysis
This is the repository to work. Analyze the World-Bank dataset of north and central America.

Feel free to add any type of file inside here: Python, Jupyter Notebook, Excel, Images.

Before submitting to Master, let's make sure anyone aproves in order to check for errors or corrections

Group 1:
Poverty
Education

Group 2:
Health
Infraestructure

Group 3:
Public sector
Social protection
Economic policy
Environment


import pandas as pd
import matplotlib.pyplot as plt

file='WDIW Dataset.xlsx'

data=pd.read_excel(file)

data.shape
country=['Belize','Bermuda','Canada','Costa Rica','El Salvador','Guatemala','Honduras','Mexico','Nicaragua','Panama','United States']

for names in country:
    




