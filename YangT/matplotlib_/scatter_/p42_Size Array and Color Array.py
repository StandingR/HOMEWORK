import matplotlib.pyplot as plt
import numpy as np

n_data = 10
x_data = np.linspace(0,10, n_data)
y_data = np.linspace(0,10, n_data)

s_arr = np.linspace(10, 500, n_data)
c_arr =[(c/n_data, c/n_data, c/n_data) for c in range(n_data)]

fig,ax = plt.subplots(figsize=(10,10))
ax.scatter(x_data,y_data,
           s=s_arr,
           c=c_arr)

plt.show()