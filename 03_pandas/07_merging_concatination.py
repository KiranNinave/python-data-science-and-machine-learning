import pandas as pd

# its like sql

df1 = pd.DataFrame(data={'A': [1,2,3], 'B': [4,5,6]}, index=[1,2,3])

df2 = pd.DataFrame(data={'A': [1,2,3], 'B': [4,5,6]}, index=[4,5,6])

df3 = pd.DataFrame(data={'A': [1,2,3], 'B': [4,5,6]}, index=[7,8,9])

print(pd.concat(objs=[df1, df2, df3])) 

print(pd.merge(left=df1, right=df2, how="inner", on="A")) # it's like joins in sql

print(df1.join(df2, how='inner', lsuffix="left", rsuffix='right'))