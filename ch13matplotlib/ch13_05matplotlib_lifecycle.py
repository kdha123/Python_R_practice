import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# 원본 데이터
data = {'Barton LLC': 109438.50,
        'Frami, Hills and Schmidt': 103569.59,
        'Fritsch, Russel and Anderson': 112214.71,
        'Jerde-Hilpert': 112591.43,
        'Keeling LLC': 100934.30,
        'Koepp Ltd': 103660.54,
        'Kulas Inc': 137351.96,
        'Trantow-Barrows': 123381.38,
        'White-Trantow': 135841.99,
        'Will LLC': 104437.60}
# 값의 리스트
group_data = list(data.values())
# 항목이름 리스트
group_names = list(data.keys())
# 값의 평균
group_mean = np.mean(group_data)


def currency(x, pos):
    """The two args are the value and tick position"""
    if x >= 1e6:
        s = '${:1.1f}M'.format(x*1e-6)
    else:
        s = '${:1.0f}K'.format(x*1e-3)
    return s


formatter = FuncFormatter(currency)

plt.rcParams.update({'figure.autolayout': True})
fig, ax = plt.subplots(figsize=(8, 8))
# matplotlib 에 데이터 셋팅
ax.barh(group_names, group_data)
# 항목이름객체(xticklabel)
labels = ax.get_xticklabels()

plt.style.use('fivethirtyeight')
# 항목에 대한 설정 적용
plt.setp(labels, rotation=45, horizontalalignment='right')
# 평균 표시
ax.axvline(group_mean, ls='--', color='r')

# 새로운 회사 표시 위치
for group in [3, 5, 8]:
    # ax.text(데이터의 값을 기준으로한 위치, 한개의 데이터, 표시할 텍스트, 폰트사이트, 정렬)
    ax.text(145000, group, "New Company", fontsize=10,
            verticalalignment="center")
# title의 위치
ax.title.set(y=1.05)
# 제목에 해당되는 것을 셋팅
ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
       title='Company Revenue')
# x 좌표 값 표시
ax.xaxis.set_major_formatter(formatter)
# x 좌표 구간의 값
ax.set_xticks([0, 25e3, 50e3, 75e3, 100e3, 125e3])
fig.subplots_adjust(right=0.126)

plt.show()
