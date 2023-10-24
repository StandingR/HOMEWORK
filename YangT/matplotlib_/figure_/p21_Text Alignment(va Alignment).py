import matplotlib.pyplot as plt

figsize=(7,7)
fig, ax = plt.subplots(figsize=figsize)

#ax.set_xlim=하는 실수 조심할것,
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.grid()
ax.tick_params(axis='both',
               labelsize=15)
"""
ax.text(x=0,y=0,
        va='top', ha ='center',
        s="Hello",
        fontsize=30)



ax.text(x=0,y=0,
        va='center', ha='center',
        s="Hello",
        fontsize=30)
"""

ax.text(x=0,y=0,
        va='center', ha='center',
        s='Hello',
        fontsize=30)


plt.show()