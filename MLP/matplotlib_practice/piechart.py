import matplotlib.pyplot as plt

categories = ["A","B","C","D","E"]
values = [23,45,12,67,37]

explode = [0,0.4,0,0,0]
plt.pie(values, labels=categories, autopct="%1.1f%%", explode=explode, shadow=True)
plt.show()
