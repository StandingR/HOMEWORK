import matplotlib.pyplot as plt

figsize = (7, 7)
fig, ax = plt.subplots(figsize=figsize)


# x ax에 대한 타이틀
ax.set_xlabel("X lable",
              fontsize=20,
              color='darkblue',
              alpha= 0.7)

# y ax에 대한 타이틀
ax.set_ylabel("Y lable",
              fontsize=20,
              color='darkblue',
              alpha=0.7)

plt.show()