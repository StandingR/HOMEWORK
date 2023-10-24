# fig.suptitle and ax.set_title(Title of Ax)

import matplotlib.pyplot as plt

figsize = (7,7)
fig, ax = plt.subplots(figsize=figsize)

# 한 ax에만 이름 넣기 - 타이틀은 따로임
#ax.set_title("Title of a AX")

"""
ax.set_title("Title of a AX",
             fontsize=30)
"""
# ax 타이틀, 글자 크기. 폰트 결종
ax.set_title("Title of a Ax",
             fontsize=30,
             fontfamily='monosapce')

plt.show()