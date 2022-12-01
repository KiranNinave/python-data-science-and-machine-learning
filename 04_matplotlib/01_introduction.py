# matplotlib is the most popular plotting library for python
# it gives you control over every aspect of figure
# it was designed to have a similar feel to MatLab's graphical plotting.

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(start=0, stop=5, num=11)
y = x ** 2

plt.subplot(1,2,1)
plt.plot(x, y, 'r')

plt.xlabel("X label")

plt.ylabel("Y label")

plt.title("Title")

# plt.show()

# creating multiple subplots
plt.subplot(1,2,2)
plt.plot(y, x, 'b')

plt.show()
