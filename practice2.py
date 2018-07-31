#coding:utf-8

import pymysql
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False    #用来正常显示负号

pd.set_option('display.width', 2000, 'display.max_rows', None,'display.max_columns', None)  # 设置数据显示


conn1=pymysql.Connect(host="127.0.0.1",
                      user="root",
                      password="HeFeng147896325",
                      port=3306,
                      db="meteorology",
                      charset="utf8")

cursor1=conn1.cursor()

sql1 = "SELECT * FROM ferrara"
cursor1.execute(sql1)
read1=list(cursor1.fetchall())
sql2="SHOW FULL COLUMNS FROM ferrara"
cursor1.execute(sql2)
read2=list(cursor1.fetchall())
ls2=[]
for i in read2:
    ls2.append(list(i)[0])
df1=pd.DataFrame(read1,columns=ls2).set_index('sort')

print(df1)

cursor1.close()
conn1.close()