import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# seaborn 차트의 배경 등 설정
sns.set(style="white", palette="muted", color_codes=True)
rs = np.random.RandomState(10)
print(rs, type(rs))

# Set up the matplotlib figure
f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)
print(f, axes)
sns.despine(left=True)

# Generate a random univariate dataset
# 표준 분포 랜덤 데이터
d = rs.normal(size=100)

# Plot a simple histogram with binsize determined automatically
# 막대그래프
sns.distplot(d, kde=False, color="b", ax=axes[0, 0])

# Plot a kernel density estimate and rug plot
# 분포에 대한 표식 : rug=True, 막대그래프 표시 hist=True(기본값)
sns.distplot(d, hist=False, rug=True, color="r", ax=axes[0, 1])

# Plot a filled kernel density estimate
# kde_kws={"shade": True} : 안쪽 면색을 지정
sns.distplot(d, hist=False, color="g", kde_kws={"shade": True}, ax=axes[1, 0])

# Plot a histogram and kernel density estimate
sns.distplot(d, color="m", ax=axes[1, 1])

# 그래프 제목, 라벨 셋팅
plt.setp(axes, yticks=[])
plt.tight_layout()

plt.show()
