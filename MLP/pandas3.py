import pandas as pd
from sklearn.datasets import load_diabetes
import numpy as np
np.random.seed(37)

diabetes = load_diabetes(as_frame=True)
df = diabetes['data']

s = pd.Series(np.random.rand(10))

'''
#.loc, .iloc

print(df.iloc[0:5])
print(df.loc[0])

#conditional selection
print(df['age'] > 0)
print(df[df['age'] > 0])
print(df.loc[df['age'] > 0])

print(df.loc[(df['age'] > 0) & (df['sex'] < 0)])
print(df.loc[(df['age'] > 0) | (df['sex'] > 0)])

print(df['age'].mean())


print(df['age'][0])

#df = df.set_index('age')
df = df.set_index('age', drop=False)
print(df)
print(df.loc[0.038075906433423026])
df = df.reset_index(drop=True)
print(df)


#df[df['age'] < 0]['sex'] = 0
df.loc[df['age'] < 1, 'sex'] = 0
print(df)


subset = df[df['age'] < 0].copy()
subset['sex'] = 0
print(subset)


print(df.mean())
print(df.mean(axis=1))
df['avg'] = df.mean(axis=1)
print(df)


print(df.drop('age', axis=1))
print(df.drop(0, axis=0))

df['New col'] = df["age"]*100
print(df)

df['New col'] = df['age'] + df['sex']

listA = range(440)
listA = np.nan(listA)

df['New col'] = listA

print(df['age'][0])
print(df['age'].isin([0.038075906433423026]))

print(df.sample(n=5))

print(df.sample(n=5, random_state=37))

print(df.sample(n=10, replace=True))

print(df['age'] == 0.038075906433423026)

print(df[df['age'] == 0.038075906433423026])
print((s.mean(), s.sum(), s.std(), s.min(), s.max(), s.count()))

'''

np.random.seed(37)

diabetes = load_diabetes(as_frame=True)
df = diabetes['data']

s = pd.Series(np.random.rand(10))

df = pd.DataFrame({
        "A": np.random.rand(5),
        "B": np.random.rand(5)
})

print(df.mean(axis=0))
print(df.mean(axis=1))



