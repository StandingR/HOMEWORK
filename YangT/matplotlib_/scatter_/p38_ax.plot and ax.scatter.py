import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

n_data = 100
x_data = np.random.normal(0,1,(n_data,))
y_data = np.random.normal(0,1,(n_data,))

fig, ax = plt.subplots(figsize=(7, 7))

#scatter 함수 이용해서 scatter plot 생성
#ax.scatter(x_data, y_data,
#           s=100)

#ax.plot에서 'o'를 이용해서 scatter plot 생성
ax.plot(x_data, y_data,
        'o',
        markersize=10)

plt.show()