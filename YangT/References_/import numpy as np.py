import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# 데이터 불러오기
iris = load_iris()

# 변수 이름 설정하기
feature_names = iris.feature_names
n_feature = len(feature_names)
species = iris.target_names
n_species = len(species)

iris_X, iris_y = iris.data, iris.target

# 데이터 추출
data = [iris_X[iris_y == i] for i in range(n_species)]

# 전체 figure와 subplot 만들기
fig, axes = plt.subplots(2, 2, figsize=(7, 7))

# 그래프 한개씩 조건 설정하기
titles = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
for i, ax in enumerate(axes.flat):
    ax.violinplot(data[i])
    ax.set_title(titles[i])
    ax.set_xticks(np.arange(1, n_species + 1))
    ax.set_xticklabels(species)

plt.tight_layout()
plt.show()
