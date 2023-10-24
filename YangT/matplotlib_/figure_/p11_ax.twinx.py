import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 10))

ax1 = fig.add_subplot()
ax2 = ax1.twinx()

#한개의 x축(ax1)을 공유하는 쌍둥이 축(Y_lim)을 만든다.
#ax1.set_xlim([0, 100])
#plt.show()



# 한개의 ax1_xlim에 쌍둥이 축 : y_lim생성 각 눈금의 숫자를 다르게 생성
"""
ax1.set_xlim([0,100])
ax1.set_ylim([0,100])
ax2.set_ylim([0,0.1])

plt.show()
"""

ax1.set_xlim([0,100])
ax1.set_ylim([0,100])
ax2.set_ylim([0,0.1])

ax1.set_title("Twinx Graph", fontsize=30)
ax1.set_ylabel("Data1",fontsize=20)
ax2.set_ylabel("Data2",fontsize=20)

fig.tight_layout()
plt.show()