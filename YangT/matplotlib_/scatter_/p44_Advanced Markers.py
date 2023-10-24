import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(5,5))

ax.scatter(0, 0,
           s=10000)

ax.scatter(0, 0,
           s=10000,
           facecolor='r')
ax.scatter(0,0,
           s=10000,
           facecolor='red',
           edgecolor='b')
ax.scatter(0, 0,
           s=10000,
           facecolor='red',
           edgecolor='b',
           linewidth=5)

plt.show()