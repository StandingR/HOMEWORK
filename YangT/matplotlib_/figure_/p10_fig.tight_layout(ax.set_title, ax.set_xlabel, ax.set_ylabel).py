import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 7))

ax.set_title('Title',fontsize=20)
ax.set_xlabel('X Label',fontsize=15)
ax.set_ylabel('Y Label',fontsize=15)

fig.tight_layout()
plt.show()