import matplotlib.pyplot as plt
import numpy as np

PI = np.pi
t = np.linspace(-4*PI, 4*PI, 300)
sin = np.sin(t)

fig, ax = plt.subplots(figsize=(10,7))

ax.plot(t, sin,
        color='black')

ax.axhline(y=1,
           linestyle=':',
           color='red')

ax.axhline(y=-1,
           linestyle=':',
           color='blue')

plt.show()