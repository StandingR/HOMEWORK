# fig.suptitle and ax.set_title(Title of Figure)

import matplotlib.pyplot as plt

# figure의 크기 = 도화지의 크기
figsize = (7,7)
fig, ax = plt.subplots(figsize=figsize)

# 타이틀 끌씨 만들기
#fig.suptitle("TItle of a Figure")

# 타이틀에 글쓰고 글자 크기 키우기(30)
#fig.suptitle("Title of a Figure",
#             fontsize=30)

# 타이틀 이름 쓰고 글자크기, 글자 폰트
fig.suptitle("Title of a Figure",
             fontsize=30,
             fontfamily = 'monspace')

plt.show()