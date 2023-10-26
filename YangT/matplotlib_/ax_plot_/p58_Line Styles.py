import matplotlib.pyplot as plt
import numpy as np

x_data = np.array([0,1])
y_data = x_data

fig, ax =plt.subplots(figsize=(10,10))

ax.plot(x_data, y_data)

ax.plot(x_data, y_data+1,
        linestyle='dotted')

ax.plot(x_data, y_data+2,
        linestyle='dashed')

ax.plot(x_data, y_data+3,
        linestyle='dashdot')

plt.show()