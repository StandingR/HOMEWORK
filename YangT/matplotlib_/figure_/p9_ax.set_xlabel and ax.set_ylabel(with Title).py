import matplotlib.pyplot as plt

figsize = (7,7)
fig, ax = plt.subplots(figsize=figsize)

fig.suptitle("Title of a Figure",
             fontsize=30,
             color='darkblue',
             alpha=0.9)

ax.set_xlabel("X lable",
              fontsize=30,
              color='darkblue',
              alpha=0.7)
ax.set_ylabel("Y lable",
              fontsize=20,
              color='darkblue',
              alpha=0.7)

plt.show()