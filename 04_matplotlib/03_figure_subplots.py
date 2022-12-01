import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(start=0, stop=5, num=11)
y = x ** 2

fig, axes = plt.subplots(nrows=1, ncols=2) # the way we can plot multiple subplots using axis
axes[0].plot(x, y)
axes[1].plot(y, x)
plt.tight_layout()
plt.show()