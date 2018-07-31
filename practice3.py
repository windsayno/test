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
# # fig.tight_layout()                  # 调整整体空白
# plt.subplots_adjust(bottom=0.06,top=0.94,left=0.08,right=0.94,wspace =0.36, hspace =0.5)       # 设置作图范围、子图间距。


df_milano=pd.read_csv("milano_270615.csv")

x1= df_milano['day'].values
x1= [datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in x1]
y1= df_milano['temp']
ax=fig.add_subplot(111)
plt.xticks(rotation=70 )
ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
ax.xaxis.set_major_locator(mdates.HourLocator())
# ax.set_xticks(x1)
# plt.gcf().autofmt_xdate()  # 自动旋转日期标记
ax.plot(x1,y1,'r')

plt.show()