from matplotlib import pylab as plt
import numpy as np
# a = 0~49, c = randint(0~49까지 50개), d(가우시안 표준정규분포): randn(-1~1 랜덤으로 50개)
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
# y 좌표에 값 분포도 * 10
data['b'] = data['a'] + 10 * np.random.randn(50)
# d -> 동그라미의 크기 : 항상 +값만 가진다. -> 절댓값으로
data['d'] = np.abs(data['d']) * 100
print(data)
# plt.scatter(x 좌표값 키, y좌표값 키, c=컬러키, s=사이즈 키, data={}딕셔너리데이터)
plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()
