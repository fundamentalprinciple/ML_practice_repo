import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
n=200

recipe_number = np.arange(1,n+1)
id = np.random.randint(1000,2000,n)

thumbs_up_count = np.random.randint(0,500,n)

best_score = thumbs_up_count*0.05 + np.random.normal(0,2,n)

rating = 5 - recipe_number*0.01 + np.random.normal(0,0.5,n)

data = pd.DataFrame({
    "recipe_number": recipe_number,
    "id": id,
    "thumbs_up_count": thumbs_up_count,
    "best_score": best_score,
    "rating": rating
})

#print(data.head())

exploration_set = data[['recipe_number',
                        'id',
                        'thumbs_up_count',
                        'best_score',
                        'rating']]

cor_matrix = exploration_set.corr(method='pearson')
#print(cor_matrix)

'''
plt.figure(figsize=(8,6))
sns.heatmap(cor_matrix,
            annot=True,
            cmap="coolwarm",
            fmt=".2f")
'''

'''
sns.scatterplot(
    x='thumbs_up_count',
    y='best_score',
    hue='rating',
    data=data
)
'''

'''
data.hist(bins=50, figsize=(12,10))
'''

sns.pairplot(data, diag_kind='hist')

plt.title("Correlation matrix heatmap")
plt.show()























