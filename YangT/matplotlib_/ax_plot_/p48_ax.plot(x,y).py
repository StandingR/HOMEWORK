import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

x_data = np.random.normal(0,1, (10, ))
y_data = np.random.normal(0,1, (10, ))

fig, ax = plt.subplots(figsize=(10,10))
ax.plot(x_data, y_data)

plt.show()