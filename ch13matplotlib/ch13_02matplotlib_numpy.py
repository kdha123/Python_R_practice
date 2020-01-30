from matplotlib import pylab as plt
import numpy as np

# 0 ~ 5까지 0.2단위로
# np.arange(시작값, 종료값(미포함), 증감값) -> 리스트 데이터 만든다.
t = np.arange(0., 5., 0.2)

# 3개의 데이터를 한꺼번에 넣어서 그래프로 표시되도록 셋팅
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
