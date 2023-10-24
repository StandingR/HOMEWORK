#안된이유는 띄어쓰기

import matplotlib.pyplot as plt


fig, ax = plt.subplots(figsize=(7, 7))

"""
ax.tick_params(labelsize=20,
               lenght=10,
               width=3,
               bottom=False,labelbottom=False)
"""

ax.tick_params(labelsize=20,
               length=10,
               width=3,
               bottom=False,
               labelbottom=False)
plt.show()