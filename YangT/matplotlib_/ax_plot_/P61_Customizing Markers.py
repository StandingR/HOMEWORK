import matplotlib.pyplot as plt
import numpy as np

PI = np.pi
#100개 여야 똑같이 나옴
t = np.linspace(-4*PI, 4*PI, 100)
sin = np.sin(t)

fig, ax = plt.subplots(figsize=(10,7))

ax.plot(t, sin+1,
        marker='o',
        color='black',
        markersize=15,
        markerfacecolor='r',
        markeredgecolor='b',
        markeredgewidth=3)

plt.show()