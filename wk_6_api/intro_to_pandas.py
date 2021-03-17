# %%
import pandas as pd

recalls = {
    'total_recalls': [34, 67, 89, 120, 56],
    'severe_recalls': [13, 40, 67, None, 40],
    'model': ['focus', 'ranger', 'f-150', None, None]
}

year_index = [2001, 2002, 2003, 2004, 2005]
df = pd.DataFrame(data=recalls, index=year_index)
print(df)


print(df.describe())


print(df.dtypes)


print(df['total_recalls'].std())

# gives size of dataframe
print(df.size)
# print(df['total_recalls'].plot(kind='bar'))
