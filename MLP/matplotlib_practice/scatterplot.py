import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y1 = [2,4,6,8,10]
y2 = [1,4,9,16,25]

plt.scatter(x,y1, color="red", marker="*", s=20)
plt.scatter(x,y2, color="blue", marker=".", s=20)
plt.show()

