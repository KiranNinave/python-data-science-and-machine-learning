# multi index
import numpy as np
import pandas as pd

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside, inside))

print("hier_index", hier_index)

hier_index = pd.MultiIndex.from_tuples(hier_index)

print("hier_index", hier_index)

df = pd.DataFrame(np.random.randn(6,2), index=hier_index, columns=["A", "B"]) # multi index data frame

print("df", df)

print("df.loc['G1']", df.loc['G1'])

print("df.loc['G1']", df.loc['G1']['A'])

print("df.index", df.index)

df.index.names = ["GROUPS", "NUM"]

print("df_renamed_index", df)