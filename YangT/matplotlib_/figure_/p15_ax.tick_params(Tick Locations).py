import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 7))


"""
ax.tick_params(labelsize=20,
               length=10,
               width=3,
               bottom=False, labelbottom=False,
               top=True, labeltop=True)
"""

ax.tick_params(labelsize=20,
               length=10,
               width=3,
               bottom=False, labelbottom=False,
               left=False, labeltop=True,
               right=True, labelright=True)

plt.show()