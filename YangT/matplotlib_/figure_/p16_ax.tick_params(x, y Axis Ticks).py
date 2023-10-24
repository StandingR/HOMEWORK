import matplotlib.pyplot as plt

fig, ax = plt.subplots (figsize=(7,7))

"""
ax.tick_params(labelsize=20,
               length=10,
               width=3,
               rotation=30)

# rotaion은 회전을 의미, axis x축 변경
ax.tick_params(axis='x',
               labelsize=20,
               length=10,
               width=3,
               rotation=30)

"""

# y축 변경
ax.tick_params(axis='y',
               labelsize=20,
               length=10,
               width=3,
               rotation=30)


plt.show()