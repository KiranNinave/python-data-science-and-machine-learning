import matplotlib.pyplot as plt
import numpy as np

figure = plt.figure() # figure is a blank canvas where we can add axis

x = np.linspace(start=0, stop=5, num=11)
y = x ** 2

axes = figure.add_axes([0.1,0.1,0.8,0.8])
axes2 = figure.add_axes([0.2, 0.5, 0.4, 0.3])

axes.set_xlabel("X Label")
axes.set_ylabel("Y Label")
axes.set_title("Set Title")
axes.plot(x,y)
axes2.plot(y, x)

plt.show()