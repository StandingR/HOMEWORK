import matplotlib.pyplot as plt

figsize=(7,7)
fig, ax = plt.subplots(figsize=(14,7))

xticks = [i for i in range(0, 101, 20)]
ax.set_xticks(xticks)

ax.tick_params(axis='x',
               labelsize=20,
               length=10,
               width=3,
               rotation=30)

plt.show()