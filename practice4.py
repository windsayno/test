# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

plt.rcParams['font.sans-serif']=['SimHei']      # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False    # 用来正常显示负号

fig=plt.figure(figsize=(12,6))       # 定义图并设置画板尺寸
fig.set(alpha=0.2)                  # 设定图表颜色alpha参数
# fig.tight_layout()                  # 调整整体空白
plt.subplots_adjust(bottom=0.12,top=0.94,left=0.08,right=0.94,wspace =0.36, hspace =0.5)       # 设置作图范围、子图间距。

ravenna=pd.read_csv('WeatherData/ravenna_270615.csv')
faenza=pd.read_csv('WeatherData/faenza_270615.csv')
cesena=pd.read_csv('WeatherData/cesena_270615.csv')
milano=pd.read_csv('WeatherData/milano_270615.csv')
asti=pd.read_csv('WeatherData/asti_270615.csv')
torino=pd.read_csv("WeatherData/torino_270615.csv")
mantova=pd.read_csv("WeatherData/mantova_270615.csv")
bologna=pd.read_csv('WeatherData/bologna_270615.csv')
piacenza=pd.read_csv('WeatherData/piacenza_270615.csv')
ferrara=pd.read_csv('WeatherData/ferrara_270615.csv')


x1=ravenna['day']
x1= [datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in x1]
y1=ravenna['temp']

x2 =faenza['day']
x2= [datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in x2]
y2 =faenza['temp']

x3 = cesena['day']
x3= [datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in x3]
y3 =cesena['temp']

x4 = milano['day']
x4= [datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in x4]
y4 = milano['temp']

x5 = asti['day']
x5= [datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in x5]
y5 = asti['temp']

x6 = torino['day']
x6= [datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in x6]
y6 = torino['temp']

x7=mantova["day"]
x7=[datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in x7]
y7=mantova["temp"]

x8=bologna["day"]
x8=[datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in x8]
y8=bologna["temp"]

x9=piacenza["day"]
x9=[datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in x9]
y9=piacenza["temp"]

x10=ferrara["day"]
x10=[datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in x10]
y10=ferrara["temp"]


# 六个城市气温日变化
ax1=fig.add_subplot(221)
ax1.set(title=u"子图标题",xlabel=u"x轴标题",ylabel=u"y轴标题")   # 设置标题
# ax1.axis([0,4,0,600])     # 设置坐标范围
ax1.xaxis.set_major_formatter(mdates.DateFormatter("%H:%S"))  # 设置横坐标时间标签格式
plt.xticks(rotation=70)        # 设置横坐标标签旋转角度
plt.plot(x1,y1,'r', x2,y2,'r',x3,y3,'r')
plt.plot(x4,y4,'g',x5,y5,'g',x6,y6,'g')
plt.legend(["ravenna","faenza","cesena","milano","asti","torino"],loc=1)


# 各城市日最高气温
ax2=fig.add_subplot(222)
# ax2.xaxis.set_major_formatter(mdates.DateFormatter("%H:%S"))
ax2.set(title=u"各城市日最高气温与距离",xlabel=u"城市与海边距离",ylabel=u"日最高气温")   # 设置标题
# ax2.axis()     # 设置坐标范围
dist=[ravenna.dist[0],faenza.dist[0],cesena.dist[0],milano.dist[0],asti.dist[0],\
      torino.dist[0],mantova.dist[0],bologna.dist[0],piacenza.dist[0],ferrara.dist[0],]
max_temp=np.array([y1.max(),y2.max(),y3.max(),y4.max(),y5.max(),y6.max(),y7.max(),y8.max(),y9.max(),y10.max()])

plt.plot(dist,max_temp,"ro")

# 回归
from sklearn.svm import SVR
svr_lin1= SVR(kernel='linear', C=1e3)
svr_lin2 = SVR(kernel='linear', C=1e3)
svr_lin1.fit(x1, y1)
svr_lin2.fit(x2, y2)
xpl = np.arange(lO,lOO,l0).reshape((9,1))
xp2 = np.arange(50,40,50).reshape((7,1))
ypl = svr_lin1.predict(xp1)
yp2 = svr_lin2.predict(xp2)
plt.plot(xp1, yp1, c='r', label='Strong sea effect')
plt.plot(xp2, yp2, c='b',label='Light sea effect')
plt.axis((0,40,27,32))
plt.scatter(x,y, c='k',lable="data")

plt.show()