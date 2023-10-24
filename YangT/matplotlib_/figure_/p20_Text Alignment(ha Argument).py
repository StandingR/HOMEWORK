import matplotlib.pyplot as plt

figsize=(7 ,7)
fig, ax = plt.subplots(figsize=figsize)

ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])

ax.grid()
ax.tick_params(axis='both',
               labelsize=15)
# 이전 코드에서 축 가져와야 함!
"""
ax.text(x=0,y=0,
        va='center', ha ='left',
        s="Hello",
        fontsize=30)
"""

"""
ax.text(x=0,y=0,
        va='center', ha='center',
        s='Hello',
        fontsize=30)
"""

ax.text(x=0,y=0,
        va='center', ha='right',
        s="Hello",fontsize=30)


plt.show()