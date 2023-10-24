import matplotlib.pyplot as plt

figsize=(7,7)
fig, ax = plt.subplots(figsize=(figsize))

#ax.tick_params(labelsize=20)
xticks = [i for i in range(10)]

ax.set_xticks(xticks)
ax.tick_params(labelsize=20)

plt.show()
