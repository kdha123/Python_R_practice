import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 그래프의 바탕격자셋팅
sns.set(style="darkgrid")

# 데이터 가져오기
fmri = sns.load_dataset("fmri")
# 데이터 셋팅
print(type(fmri.timepoint))

# sns.relplot(x="timepoint", y="signal", kind="line", data=fmri)
sns.relplot(x="timepoint", y="signal", ci=None, kind="line", data=fmri)
plt.show()
