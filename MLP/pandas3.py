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

print(df.mean(axis=0))
print(df.mean(axis=1))


'''

'''
np.random.seed(37)

diabetes = load_diabetes(as_frame=True)
df = diabetes['data']

s = pd.Series(np.random.rand(10))

df = pd.DataFrame({
        "A": np.random.rand(5),
        "B": np.random.rand(5)
})

df = pd.DataFrame({
    "key": ["A", "B", "C", "A", "B", "C"],
    "x": [0, 1, 2, 3, 4, 5],
    "y": [10, 20, 30, 40, 50, 60]
})

g = df.groupby("key")

print(df)
print(type(g))
print(g)
print((g.sum(), g.mean(), g.count(), g.min(), g.max()))
'''

'''
df = pd.Series([180, 175, 168, 190], index=["A","B","C","D"])

def convert(cm):
    return cm*0.0328084
print(df.apply(convert))
'''

'''
df = pd.DataFrame({"name": ["John Doe", "Dohn Joe"]})

print(df)

def first_name(s):
    return s.split()[0]

df["FirstName"] = df["name"].apply(first_name)
print(df)
'''

'''
df = pd.Series(["A","B","A","C"])
mapping = {"A":4, "B":3, "C":2}
print(df.map(mapping))
'''

'''
df1 = pd.DataFrame({
            "col1":[1,2,3],
            "col2":[4,5,6]
    })

df2 = pd.DataFrame({
            "col1":[7,8,9],
            "col4":[10,11,12]
    })
print(pd.concat([df1,df2], axis=0, keys=["A","B"], join="inner"))
print(pd.concat([df1,df2], axis=1, keys=["A","B"], join="inner"))
'''

'''
df1 = pd.DataFrame({
            "col1": [1,2,3],
            "col2": [4,5,6]
})

df2 = pd.DataFrame({
            "col1": [1,2,3],
            "col2": [7,8,9]
})

print(df1.compare(df2))
print(df1.compare(df2, keep_equal=True))
'''

data = {
    "Date": ['2022-01-01', '2022-01-01', '2022-01-02', '2022-01-02'],
    "Category": ['A', 'B', 'A', 'B'],
    "Value": [10,20,30,40]
}
df = pd.DataFrame(data)
print(df)

df_pt = df.pivot_table(
    values="Value",
    index="Date",
    columns="Category",
    aggfunc = "mean",
    fill_value = 0
)

print(df_pt)
