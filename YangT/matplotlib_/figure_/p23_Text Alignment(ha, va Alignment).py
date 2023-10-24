import matplotlib.pyplot as plt
import numpy as np

figsize=(15,10)
fig,ax = plt.subplots(figsize=figsize)

space_1 = ax.text1(x=0, y=0, va = 'bottom', ha = 'right', s='Hello',fontsize=30)
space_2 = ax.text2(x=0, y=0, va = 'bottom', ha = 'left', s='Hello',fontsize=30)
space_3 = ax.text3(x=0, y=0, va = 'top', ha = 'right', s='Hello',fontsize=30)
space_4 = ax.text4(x=0, y=0, va = 'top', ha = 'right', s='Hello',fontsize=30)

"""
plt.subplot(ax.text1,2,2,1)
plt.title('subtitle_one')
plt.plot(space_1)
plt.subplot(ax.text2,2,2,2)
plt.plot(space_2)
plt.title('subtitle_two')
plt.subplot(ax.text3,2,2,3)
plt.plot(space_3)
plt.title('subtitle_three')
plt.subplot(ax.text4,2,2,4)
plt.plot(space_4)
plt.title('subtitle_four')
"""
plt.show()