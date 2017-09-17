import pandas as pd
import numpy as np
data = pd.read_csv("data/beauty.csv", sep=";");
# type(data)
# print(data.head())
# print(data.shape)
# print(data.info())
# print("describe ----- !")
# print(data.describe())

# print(data.sort_values(['exper']))
# print(data["exper"].
#       sort_values().
#       head())
#
#
# print(data.loc[5:5,["exper","union"]])
# print(data.iloc[:,3:5])
print(data[(data["female"] == 1) & (data["married"] == 1)].head()["wage"].mean(),
      data[data["female"] == 0].head()["wage"].mean())

for rowNum, sub_df in data.groupby("looks"):
    print(rowNum, sub_df["wage"].median(),sub_df["female"].mean())


print(data.groupby('looks')[['wage', 'exper']].agg(np.median))


print(pd.crosstab(data['female'], data['married']))


print(data["wage"].describe())


data['is_rich'] = (data['wage'] > data['wage'].quantile(0.75)).astype('int64')

print(data.head())