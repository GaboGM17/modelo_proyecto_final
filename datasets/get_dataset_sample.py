import pandas as pd

df = pd.read_csv('housing_df.csv')

sample_row = df.drop(['MEDV'], axis=1).sample(1).iloc[0].to_dict()

print(sample_row)

#%%
