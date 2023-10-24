import matplotlib.pyplot as plt
import numpy as np

# 랜덤시드 0으로 설정해서 튀는 값 막아줌
np.random.seed(0)

# x의 범위 설정
x_min, x_max = -5,5
n_data = 300

#uniform = 균등분포에서 포본을 추출하는 함수
x_data = np.random.uniform(x_min, x_max, n_data)
y_data = x_data + 0.5*np.random.normal(0,1,n_data)

# linspace를 이용해서 간격2만큼 min,max에 범위에서 출력
pred_x = np.linspace(x_min, x_max, 2)
pred_y = pred_x

# fig,ax 만들어주기
fig, ax = plt.subplots(figsize=(10,10))
ax.scatter(x_data,y_data)

ax.plot(pred_x, pred_y,
        color='r',
        linewidth=3)

plt.show()
