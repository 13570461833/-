import pandas as pd
import os
import matplotlib.pyplot as plt
os.chdir(r'D:\大学\泰迪销售项目\项目数据')
data5=pd.read_csv('附件1.csv',encoding='gbk')
data6=pd.read_csv('附件2.csv',encoding='gbk')
datac=pd.DataFrame()
for i in range(data6['商品'].count()):
    b=data5.loc[data5['商品'].isin([data6['商品'][i]])]['商品'].count()
    A=[data6['大类'][i]]*b
    C=[data6['二级类'][i]]*b
    datab=pd.DataFrame(data5.loc[data5['商品'].isin([data6['商品'][i]])])
    datab['大类']=A
    datab['二级类']=C
    datac=datac.append(datab)    
datac.to_csv('datac.csv',encoding='gbk')
