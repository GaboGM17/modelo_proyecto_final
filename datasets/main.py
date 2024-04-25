import pandas as pd
import numpy as np

df = pd.read_csv('housing_df.csv')

new_data = pd.DataFrame({
    'CRIM': np.random.rand(5),
    'ZN': np.random.rand(5) * 100,
    'INDUS': np.random.rand(5) * 25,
    'CHAS': np.random.choice([0, 1], size=5),
    'NOX': np.random.rand(5),
    'RM': np.random.rand(5) * 5 + 3,
    'AGE': np.random.rand(5) * 100,
    'DIS': np.random.rand(5) * 10,
    'RAD': np.random.choice(np.arange(1, 25), size=5),
    'TAX': np.random.rand(5) * 500 + 200,
    'PTRATIO': np.random.rand(5) * 12 + 8,
    'B': np.random.rand(5) * 100,
    'LSTAT': np.random.rand(5) * 30,
    'MEDV': np.random.rand(5) * 50
})
df = pd.concat([df, new_data], ignore_index=True)

df.to_csv('housing_df.csv', index=False)

#%%
