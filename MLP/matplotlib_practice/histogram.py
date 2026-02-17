import matplotlib.pyplot as plt
import numpy as np

x1 = [1,1,1,2,2,3,3,3,3,3,3,4,4,4,4,2,2,2,5,5]
x2 = np.random.normal(loc=20,scale=5,size=1000)

plt.hist(x2)
plt.show()
