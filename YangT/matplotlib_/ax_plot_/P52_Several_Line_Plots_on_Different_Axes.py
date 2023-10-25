import matplotlib.pyplot as plt
import numpy as np

PI = np.pi
t = np.linspace(-4*PI, 4*PI, 1000)
tan = np.tan(t)

fig, axes = plt.subplots(figsize=(7,7))

axes.plot(t,tan)

axes[:-1][np.diff(axes)<0]  = np.nan

plt.show()