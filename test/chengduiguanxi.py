# -*- coding: UTF-8 -*-


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# 数据准备
iris = pd.read_csv("/Users/wangyuntao/datas/seaborn-data-master/iris.csv")
# 用Seaborn画成对关系
sns.pairplot(iris)
plt.show()
