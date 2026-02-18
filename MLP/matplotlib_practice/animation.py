import matplotlib.pyplot as plt
import numpy as np

n = 500
heads_count = 0

fig,ax  = plt.subplots()
ax.set_xlim(1,n)
ax.set_ylim(0,1)

ax.set_xlabel("Number of Tosses")
ax.set_ylabel("Proportion of Heads")
ax.set_title("Convergence to 0.5")

line, = ax.plot([],[])

proportions = []

for i in range(1,n+1):
    toss = np.random.randint(0,2)

    if toss == 1:
        heads_count +=1

    proportion = heads_count / i
    proportions.append(proportion)

    line.set_data(range(1,i+1),proportions)

    plt.pause(0.01)

plt.show()

