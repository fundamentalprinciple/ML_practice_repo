import pandas as pd
from sklearn.datasets import load_diabetes

diabetes = load_diabetes(as_frame=True)
df = diabetes['data']
print(df.head(n=442))
print(df.tail(n=10))
 
