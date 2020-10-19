import matplotlib.pyplot as plt

x_valus = [1, 2, 3, 4, 5]
y_values = [x ** 3 for x in x_valus]

plt.scatter(x_valus, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=200)

plt.title("Squares", fontsize=24)
plt.xlabel("x", fontsize=14)
plt.ylabel("y", fontsize=14)

plt.tick_params(axis="both", which="major" ,labelsize=14)

plt.axis([0, 6, 0, 150])

#plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')