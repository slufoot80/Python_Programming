import matplotlib.pyplot as plt

plt.scatter(2, 4)

plt.scatter(2,4, s=200)

"""Set chart title adn label axes."""
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

"""Set size of the tick labels."""
plt.tick_params(axis='both', which='major', labelsize=14)

"""Set the range for each axis"""
plt.axis([0, 1100, 0, 1100000])

"""Set the X & Y values in a list"""
x_values = list(range(1,1001,2))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.gnuplot2, edgecolor='none', s=10)

plt.show()
#plt.savefig('squares_plot.png', bbox_inches='tight')

