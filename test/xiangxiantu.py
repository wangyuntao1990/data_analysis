# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 数据准备
# 生成10*4维度数据
data = np.random.normal(size=(10, 4))
labels = ['A', 'B', 'C', 'D']
# 用Matplotlib画箱线图
plt.boxplot(data, labels=labels)
plt.show()
# 用Seaborn画箱线图
df = pd.DataFrame(data, columns=labels)
sns.boxplot(data=df)
plt.show()
