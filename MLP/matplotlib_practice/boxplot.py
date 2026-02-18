import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(200,8,1000)

plt.boxplot(x)
plt.title("Box plot example")
plt.ylabel("Values")
plt.show()


