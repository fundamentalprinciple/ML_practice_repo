import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y1 = [2,4,6,8,10]
y2 = [1,4,9,16,25]

plt.plot(x,y1, color="blue", linestyle="-.", label="x squared")
plt.plot(x,y2, color="red", linestyle="--", label="x cubed")
plt.legend()
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Just a graph")
plt.grid(True, color="black")
plt.show()
