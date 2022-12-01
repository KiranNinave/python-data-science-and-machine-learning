import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(start=0, stop=5, num=11)
y = x ** 2

# with figsize we can define figure size

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8,2))

axes[0].plot(x,y)
axes[1].plot(y,x)

plt.tight_layout()

fig.savefig("myfile.png", dpi=200) # save fig as png
plt.show()
