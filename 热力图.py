import pandas as pd
import os
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np
import seaborn as sns
plt.rcParams['font.sans-serif'] = 'SimHei'#防止中文不能显示
os.chdir(r'D:\大学\泰迪销售项目\项目数据')
dataA=pd.read_csv('task1-1C.csv',encoding='gbk')
dataA['支付时间']=pd.to_datetime(dataA['支付时间'])
dataB=dataA[(dataA['支付时间'] >=pd.to_datetime('2017-06-1 00:00')) & (dataA['支付时间'] <= pd.to_datetime('2017-06-30 23:59'))]
a='2017-06-1 00:00'
b='2017-06-1 00:59'
p='2017-06-1 00:00'
c='2017-06-1 23:59'
F=[]
for i in range(30):
    d=pd.to_datetime(a)+dt.timedelta(days=i) 
    e=pd.to_datetime(c)+dt.timedelta(days=i)
    datB=dataB[(dataB['支付时间'] >=pd.to_datetime(d)) & (dataB['支付时间'] <= pd.to_datetime(e))]
    S=[]
    for j in range(24):
        f=pd.to_datetime(p)+dt.timedelta(minutes=j*60)+dt.timedelta(days=i)
        g=pd.to_datetime(b)+dt.timedelta(minutes=j*60)+dt.timedelta(days=i)
        datC=datB[(datB['支付时间'] >=pd.to_datetime(f)) & (datB['支付时间'] <= pd.to_datetime(g))]
        D=datC['支付时间'].count()
        S.append(D)
    F.extend(S)  #计算出每小时对应的订单量
H=['01号']*24+['02号']*24+['03号']*24+['04号']*24+['05号']*24+['06号']*24+['07号']*24+['08号']*24+['09号']*24
for y in range(10,31):
    Y=[str(y)+'号']*24
    H.extend(Y)      
P=[]
for u in range(9):
    R=['0'+str(u)+'时~'+'0'+str(u+1)+'时']
    P.extend(R)
P.extend(['09时~10时'])
for o in range(10,24):
    L=[str(o)+'时~'+str(o+1)+'时']
    P.extend(L)
kx=pd.DataFrame({'日':H,'时':P*30,'数据':F})#创建出日，时，订单量三列的dataframe型数据，为了方便热力图的绘制
zk=kx.pivot_table(index='时', columns='日', values='数据', aggfunc=np.sum)  #热力图需要的数据
f,ax1= plt.subplots(figsize = (16,10),nrows=1)#设置画布大小
cmap = sns.cubehelix_palette(start = 1.5, rot = 3, gamma=0.8, as_cmap = True)
sns.heatmap(zk, linewidths = 0.05, ax = ax1, vmax=20, vmin=0, cmap=cmap) #设置颜色的分度，最值
ax1.set_title('2017年C售货机6月订单量热力图')
ax1.set_xlabel('日')
ax1.set_ylabel('时')
plt.savefig('2017年C售货机6月订单量热力图.png')#将结果以png输出
