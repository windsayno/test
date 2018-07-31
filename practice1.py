# -*- coding: utf-8 -*-

import time
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdt

plt.rcParams['font.sans-serif']=['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False    #用来正常显示负号
pd.set_option('display.width', 2000, 'display.max_rows', None,'display.max_columns', None)  # 设置数据显示

ferrara = pd.pd.read_csv("WeatherData/ferrara_270615.csv")
torino = pd.read_csv('WeatherData/torino_270615.csv')
mantova = pd.read_csv('WeatherData/mantova_270615.csv')
milano = pd.read_csv('WeatherData/milano_270615.csv')
ravenna = pd.read_csv('WeatherData/ravenna_270615.csv')
asti = pd.read_csv('WeatherData/asti_270615.csv')
bologna = pd.read_csv('WeatherData/bologna_270615.csv')
piacenza = pd.read_csv('WeatherData/piacenza_270615.csv')
cesena = pd.read_csv('WeatherData/cesena_270615.csv')
faenza = pd.read_csv('WeatherData/faenza_270615.csv')

fig=plt.figure(figsize=(12,6))       # 定义图并设置画板尺寸



ax1=fig.add_subplot(231)
plt.xticks(rotation=70)
x1=milano["day"]
y1=milano["temp"]

# hours=[]
# for i in x1:
#     hours.append(time.strptime(str(i),"%Y-%m-%d %H:%M:%S"))
#     hours[len(hours)-1]=hours[len(hours)-1].tm_hour
ax1.xaxis.set_major_formatter(mdt.DateFormatter("%H:%M"))
ax1.plot(x1,y1,"r")
'''
import matplotlib.dates as mdates
import datetime
import numpy as np
import matplotlib. pyplot as plt
events = [datetime.date(2015,1,23),datetime.date(2015,1,28),datetime.date(2015,2,3),datetime.date(2015,2,21),
          datetime.date(2015,3,15),datetime.date(2015,3,24),datetime.date(2015,4,8),datetime.date(2015,4,24)]
readings = [12,22,25,20,18,15,17,14]
months = mdates.MonthLocator()

days = mdates.DayLocator()
timeFmt =mdates.DateFormatter("%H:%M")
fig, ax = plt.subplots()
plt.plot (events, readings)
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(timeFmt)
ax.xaxis.set_minor_locator(days)
'''
plt.show()