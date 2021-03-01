# -*-coding: UTF-8-*-

import numpy as np

b = [1, 5, 9, 2, 15, 4, 12]
for i in range(0, len(b)-1):
    temp = b[i]
    for j in range(i+1, len(b)-1):
        if temp < b[j]:
            temp, b[j] = b[j], temp
    print(temp)
