import matplotlib.pyplot as plt
import numpy as np

n_data = 100
x_data = np.random.normal(0,1,(n_data,))
y_data = np.random.normal(0,1,(n_data,))

fig, ax = plt.subplots(figsize=(6,6))

ax.scatter(x_data, y_data,
           s=300,
           facecolor='white',
           edgecolor='tab:blue',
           linewidth=5)

ax.scatter(x_data, y_data,
           s=300,
           facecolor='None',
           edgecolor='tab:blue',
           linewidth=5)

plt.show()