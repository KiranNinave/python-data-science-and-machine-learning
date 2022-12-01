import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(start=0, stop=5, num=11)
y = x ** 2

fig = plt.figure()

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

axes.plot(x, x**2, label="X square", linewidth=2, color="red", marker="o", markersize=10, markerfacecolor="black")
axes.plot(x, x**3, label="X cube", lw=3, color="green", linestyle="dotted")

axes.set_xlim([0,1]) # limit x axis
axes.set_ylim([0,1]) # limit y axis

axes.legend()

# plt.tight_layout()

plt.show()