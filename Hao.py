import pandas as pd

file = 'WDIW Dataset.xlsx'
hot_rod = pd.read_excel(file)
hot_rod = hot_rod.loc[hot_rod['Cool Name'].str.contains('Hot Rod')]
print(hot_rod)
