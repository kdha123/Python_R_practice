from matplotlib import pylab as plt
import numpy as np
'''
# 도표 전체 보여지는 부분 설정
plt.figure(figsize=(10, 6))

# subplot - 부분으로 나눠서 데이터를 표시하는데 사용
# subplot(2:세로나눔, 2: 가로나눔, 1: 현재 지정 subplot의 위치)
plt.subplot(221)
plt.subplot(222)
plt.subplot(211)
plt.subplot(212)

plt.show()
'''

plt.figure(figsize=(8, 10))

t = np.arange(0, 5, 0.1)
# subplot 위치
# 루트값
plt.subplot(411)
# 데이터 셋팅
plt.plot(t, np.sqrt(t))
# 위치에 셋팅
plt.grid()

plt.subplot(423)
# 데이터 셋팅
plt.plot(t, t**2)
# 위치에 셋팅
plt.grid()

plt.subplot(424)
# 데이터 셋팅
plt.plot(t, t**3)
# 위치에 셋팅
plt.grid()

# sin
plt.subplot(413)
# 데이터 셋팅
plt.plot(t, np.sin(t))
# 위치에 셋팅
plt.grid()

plt.subplot(414)
# 데이터 셋팅
plt.plot(t, np.cos(t))
# 위치에 셋팅
plt.grid()

plt.show()
