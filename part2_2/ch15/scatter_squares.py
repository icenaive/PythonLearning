import matplotlib.pyplot as plt

x_valus = list(range(1, 1001))
y_values = [x ** 2 for x in x_valus]

plt.scatter(x_valus, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=200)

plt.title("Squares", fontsize=24)
plt.xlabel("x", fontsize=14)
plt.ylabel("y", fontsize=14)

plt.tick_params(axis="both", which="major" ,labelsize=14)

plt.axis([0, 1100, 0, 1100000])

#plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')