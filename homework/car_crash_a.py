# -*- coding: UTF-8 -*-

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

car_crash = pd.read_csv('/Users/wangyuntao/datas/seaborn-data-master/car_crashes.csv')
sns.pairplot(car_crash)
plt.show()
