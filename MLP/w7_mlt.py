import warnings
warnings.filterwarnings('ignore')
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [8, 8]
plt.rcParams['font.size'] = 15
import math


def entropy(p: float) -> float:
    """Binary entropy in bits using log2.

    Args:
        p: proportion of class-1 in the node (0 <= p <= 1)

    Returns:
        Entropy in bits. Handles p==0 or p==1 and returns 0.0 for those.
    """
    # Guard against floating point issues at the boundaries
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return - (p * math.log2(p) + (1.0 - p) * math.log2(1.0 - p))

def plot_entropy():
    p_values = [i / 100 for i in range(101)]  # p from 0 to 1 in increments of 0.01
    entropy_values = [entropy(p) for p in p_values]  # Calculate entropy for each p

    plt.plot(p_values, entropy_values)
    plt.title('Entropy as a function of p')
    plt.xlabel('Proportion of class +1 (p)')
    plt.ylabel('Entropy')
    plt.grid(True)
    plt.show()

plot_entropy()
