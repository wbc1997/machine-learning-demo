# -*- coding = utf-8 -*-
# @Time:2022/5/3 10:08
# @File : Data Generator.py
# @Software:PyCharm
import numpy as np
import matplotlib.pyplot as plt
# b=np.array([1,2,3]).reshape(-1,1)
# print(b)
# np.random.seed(0)
inputes=1
example=1000
w_true=np.array(2)
b_tyue=np.array(1)
delta=0.01
features=np.random.randn(example,inputes)
lable_true=np.power(features,2)*w_true+b_tyue
lables=lable_true+np.random.normal(size=features.shape)*delta

plt.plot(features[:,0],lables,'or')

plt.show()
