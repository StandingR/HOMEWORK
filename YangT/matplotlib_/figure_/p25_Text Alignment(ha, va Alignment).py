import matplotlib.pyplot as plt

figsize=(7,7)
fig, ax = plt.subplots(figsize=figsize)

ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.grid()
ax.tick_params(axis='both',
               labelsize=15)

ax.text(x=-4,y=4,
        va='top', ha='left',
        s='Hello1',
        fontsize=30)

ax.text(x=-4, y=-4,
        va ='bottom', ha='left',
        s='Hello3',
        fontsize=30)

ax.text(x=4, y=4,
        va='top', ha='right',
        s="Hello2",
        fontsize=30)

ax.text(x=4, y=-4,
        va='bottom',ha='right',
        s="Hello4",
        fontsize=30)

plt.tight_layout()
plt.show()