import matplotlib.pyplot as plt
import numpy as np

# 데이터의 수 정하고 linspace로 출력 인자를 조절
n_data = 10
x_data = np.linspace(0, 10, n_data)
y_data = np.linspace(0, 10, n_data)

#s_arr이로 scatter paramater s 값 채워주기
s_arr = np.linspace(10, 500, n_data)

# fig, ax로 출력
fig, ax = plt.subplots(figsize=(10,10))
ax.scatter(x_data,y_data,
           s=s_arr)

plt.show()