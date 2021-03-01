# -*- coding: UTF-8 -*-


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
# 数据准备
# flights = pd.read_csv("/Users/wangyuntao/datas/seaborn-data-master/flights.csv")
flights = sns.load_dataset("flights", data_home='/Users/wangyuntao/datas/seaborn-data-master')
data = flights.pivot('year', 'month', 'passengers')
# 用Seaborn画热力图
sns.heatmap(data)
plt.show()
