import matplotlib as mpl
import matplotlib.pylab as plt
from matplotlib import font_manager, rc

# 한글 폰트를 인식 못해서 파일을 직접 지정해서 한글을 해결한다.
malgun = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
hangodic = font_manager.FontProperties(fname="c:/Windows/Fonts/HMKMRHD.TTF").get_name()
rc('font', family=malgun)

# 그래프 셋팅
# 제목
# plt.title("Line plot", fontdict={"family": hangodic})
plt.title("년도별 데이터", family=hangodic)
# 데이터 셋팅
# x 좌표는 인덱스 값을 사용한다.
# plt.plot([1, 4, 9, 16])
# x 좌표 셋팅
# plt.plot(x축의 항목이름, 데이터, 라인속성)
# rs-- => r = red, s = square, --, - = Line style
# plt.plot(['2016', '2017', "2018", "2019"], [1, 4, 9, 16], 'rs-')
# 항목별 라인속성 지정
# 라인 속성 종류
# - ls : 선 스타일, lw: 선의 굵기, c: 선색, marker: 데이터위치의 마커(마커의 모양), ms : 마커의 크기, mec : 마커 테두리 색
#   mew : 마커 테두리 색, mfc : 마커내부 색
plt.plot(['2016', '2017', "2018", "2019"], [1, 4, 9, 16], ls='--', marker="s", mfc='r', c='r')
# x, y축의 라벨 셋팅
plt.xlabel("년도")
plt.ylabel("값")
plt.show()
