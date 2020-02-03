import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 그래프의 바탕격자셋팅
sns.set(style="darkgrid")

# seaborn의 제공 데이터 가져오기
tips = sns.load_dataset("tips")
print(tips, type(tips))
# 전체 주문 금액과 팁의 관계
# sns.relplot(x="total_bill", y="tip", data=tips)

# 흡연자/비흡연자
# sns.relplot(x="total_bill", y="tip", hue="smoker", data=tips)
# sns.relplot(x="total_bill", y="tip", hue="smoker", style="time",
# data=tips)
# 인원수에 따른 금액과 팁의 관계
sns.relplot(x="total_bill", y="tip",  hue="size", size="size", data=tips)


plt.show()
