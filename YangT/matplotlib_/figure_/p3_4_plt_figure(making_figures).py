"""

matplotlib.pyplot.figure

matplotlib.figure(num = None, dpi = None,facecolor=none, edgecolor = None, frameon = True,
FigureClass =< class 'matplotilib.figure'>, clear = False, **kwargs))

create a new figurs
"""

import matplotlib.pyplot as plt
#import numpy as np

fig = plt.figure(figsize=(7,7),
                 facecolor = 'linen')

ax = fig.add_subplot()
ax.plot([2,3,1])
ax.scatter([2,3,1],[2,3,4])

plt.show()
