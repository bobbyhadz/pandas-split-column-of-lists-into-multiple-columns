# Pandas: Split a Column of Lists into Multiple Columns

import pandas as pd

df = pd.DataFrame({
    'A': ['Alice', 'Bobby', 'Carl'],
    'B': [[1, 2], [3, 4], [5, 6]],
})

print(df)

print('-' * 50)

df[['B1', 'B2']] = pd.DataFrame(
  df['B'].tolist(),
  index=df.index
)

print(df)