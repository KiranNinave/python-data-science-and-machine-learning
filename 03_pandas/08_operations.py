import pandas as pd

df = pd.DataFrame(data={
    'col1': [1,2,3,4],
    'col2': [444,555,666,444],
    'col3': ['abc', 'def', 'ghi', 'xyz']
})

print(df.head())


print(df['col2'].unique()) # find unique value in column

print(df['col2'].nunique()) # number of unique values

print(df['col2'].value_counts()) # unique value counts

# broad casting function on column
def times_two(x):
    return x * 2
print(df['col2'].apply(times_two)) # we can apply a diffrent function to pandas data frame 

print(df['col2'].apply(lambda x: x*2)) # using lambda functions

print(df['col3'].apply(len)) # we can also apply built in functions

print(df.columns) # print column names

print(df.index) # index on row

print(df.sort_values('col2')) # sort values by column

print(df.pivot_table(values='col2', index=['col1'], columns=['col3'])) # create new df from exiting df like views in sql