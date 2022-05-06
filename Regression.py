# -*- coding = utf-8 -*-
# @Time:2022/4/30 16:32
# @File : Regression.py
# @Software:PyCharm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
# x=np.zeros((2,2,3))
# #print(np.eye(5))
# #print(x.shape)
# b=np.full_like(x,5)
# print(b)
#print(np.linspace(1,10,20))
# a=np.ones((2,3,2))
# b=a.reshape((3,4))
# print(b)
# a=np.eye(5)
# new=a.astype(np.float)
# print(new)
# plt.subplot(3,2,4)
# plt.plot([3,4,5,3],[9,2,1,4])
# plt.ylabel("y")
# plt.xlabel("x")
# #plt.savefig('test',dpi=200)
# plt.axis([-1,5,0,9])
# plt.show()
# def f(b):
#     return np.exp(-b)*np.cos(2*np.pi*b)
# a=np.arange(0,5,0.02)
# plt.subplot(211)
# plt.plot(a,f(a))
# a=np.arange(10)
# plt.plot(a,a*1.5,a,a*2.5,a,a*3.5)
# plt.show()
# a=np.arange(10)
# plt.plot(a,a*1.5,'r--',a,a*4,'g:',a,a*3,'ro')
# plt.show()
# a=np.arange(0.0,5.0,0.02)
# plt.plot(a,np.cos(2*np.pi*a),'r--')
#
# plt.xlabel('横轴：时间',fontproperties='Kaiti',fontsize=20)
# plt.ylabel('纵轴：振幅',fontproperties='Kaiti',fontsize=20)
# plt.title('正弦图像',fontproperties='Kaiti',fontsize=20)
# plt.text(2,1,'u=1',fontsize=20)
# plt.annotate('重点',xy=(1,1),xytext=(1,1.5),arrowprops=dict(facecolor='green',shrink=0.1,width=2),fontproperties='Kaiti',fontsize=20)
# plt.axis([-1,6,-2,2])
# #plt.grid(True)
# plt.show()

# plt.subplot2grid((3,3),(1,0),colspan=1)
# plt.how()
# import matplotlib.gridspec as gri
# gs=gri.GridSpec(3,3)
#
#
# ax1=plt.subplot(gs[0,:])
# plt.show()
# a=np.array([[1,2,5],[3,2,8]]).T
# b=np.corrcoef(a[:,0],a[:,1])
# print(b)
# x=np.random.randn(20)
# y=x+1
# # plt.plot(x,y,'ro')
# # plt.show()
# ran=np.random.normal(size=x.shape)
# delta=0.9
# r=delta*ran
# y1=y+r
# plt.subplot(211)
# plt.plot(x,y,'ro')
#
# plt.subplot(212)
# plt.plot(x,y1,'bo')
# plt.show()
x=np.random.randn(20)
y=x+1
ran=np.random.normal(size=x.size)
d1=[0.5,0.7,1.2,1.5,2,5]
z1=[]
v1=[]
for i in d1:
    yn=x+1+(ran*i)
    z1.append(np.corrcoef(x,yn))
    v1.append(yn)
plt.subplot(321)
plt.plot(x,v1[0],'ro')
plt.plot(x,y,'r-')

plt.subplot(322)
plt.plot(x,v1[1],'ro')
plt.plot(x,y,'r-')

plt.subplot(323)
plt.plot(x,v1[2],'ro')
plt.plot(x,y,'r-')

plt.subplot(324)
plt.plot(x,v1[3],'ro')
plt.plot(x,y,'r-')

plt.subplot(325)
plt.plot(x,v1[4],'bo')
plt.plot(x,y,'r-')

plt.subplot(326)
plt.plot(x,v1[5],'ro')
plt.plot(x,y,'r-')

plt.show()






















# plt.subplot(212)
# plt.plot(a,np.cos(2*np.pi*a),'--')
# plt.show()