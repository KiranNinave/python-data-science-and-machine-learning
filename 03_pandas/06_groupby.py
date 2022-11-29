import numpy as np
import pandas as pd

data = {
    'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
    'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa','Carl', 'Sarah'],
    'Sales': [200, 120, 340, 243, 350, 450]
}

df = pd.DataFrame(data=data)

print(df)

byComp = df.groupby("Company") # group by company

print("byComp mean", byComp.mean()) # get mean group by

print("sum", byComp.sum()) # sum

print("std", byComp.std()) # std

print("max", byComp.max().loc['FB']) # max

print("describe", byComp.describe()) # describe