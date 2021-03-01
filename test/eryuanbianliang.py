# -*- coding: UTF-8 -*-


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# 数据准备
tips = pd.read_csv("/Users/wangyuntao/datas/seaborn-data-master/tips.csv")
print(tips.head(10))
# 用Seaborn画二元变量分布图（散点图，核密度图，Hexbin图）
sns.jointplot(x="total_bill", y="tip", data=tips, kind='scatter')
sns.jointplot(x="total_bill", y="tip", data=tips, kind='kde')
sns.jointplot(x="total_bill", y="tip", data=tips, kind='hex')
plt.show()
