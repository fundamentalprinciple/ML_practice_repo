import pandas as pd

df = pd.read_csv("example.csv")

print(df)

X = df.drop("Last name", axis=1).values
y = df["Last name"].values

print(X,y)
