import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

y_data = np.random.normal(loc=0, scale=1, size=(300,))

fig, ax = plt.subplots(figsize=(10,5))
ax.plot(y_data)

fig.tight_layout(pad=3)
ax.tick_params(labelsize=25)

plt.show()