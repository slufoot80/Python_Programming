from matplotlib import pyplot as plt


"""Define Data"""
x_values = list(range(5001))
cubes = [x**3 for x in x_values]

"""Make plot."""
plt.scatter(x_values, cubes, c=cubes, edgecolor='none', cmap=plt.cm.BuGn, s=40)

"""Customize plot"""
plt.title("Cubes", fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Cube of Value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.axis([0, 5100, 0, 5100**3])

plt.show()
