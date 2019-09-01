import pandas as pd
import os
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns
N=['饼干糕点','茶饮料','方便速食','功能饮料','果冻/龟苓膏',
  '果蔬饮料','海味零食','坚果炒货','咖啡','蜜饯/果干',
   '膨化食品','其他','肉干/豆制品/蛋','乳制品','水',
  '碳酸饮料','糖果/巧克力','香烟','植物蛋白','纸巾']
y=['一月']*20+['二月']*20+['三月']*20+['四月']*20+['五月']*20+['六月']*20+['七月']*20+['八月']*20+['九月']*20+['十月']*20+['十一月']*20+['十二月']*20
kx=pd.DataFrame({'二级类':N*12,'月份':y})
plt.rcParams['font.sans-serif'] = 'SimHei'
os.chdir(r'D:\大学\泰迪销售项目\项目数据')
dataA=pd.read_csv('datac.csv',encoding='gbk')
lista=dataA.loc[dataA['地点'].str.contains('C')]
a='20170101';b='20170201';c='20170301';d='20170401';e='20170501';f='20170601';g='20170701';h='20170801';l='20170901';m='20171001';n='20171101'
o='20171201';p='20180101'
M=[a,b,c,d,e,f,g,h,l,m,n,o,p]
S=[]
for i in range(12):
        lista['支付时间']=pd.to_datetime(lista['支付时间'])
        data1 = lista[(lista['支付时间'] >=pd.to_datetime(M[i])) & (lista['支付时间'] <= pd.to_datetime(M[i+1]))]
        T=[]
        for k in range(len(N)):
            A=data1.loc[data1['二级类'].isin([N[k]])]['应付金额'].count()
            B=data1.loc[data1['二级类'].isin([N[k]])]['应付金额'].sum()
            T.append(round((B/A),2))
        S.extend(T)
kx['数据']=S
kx.fillna(0).to_csv('z.csv',encoding='gbk')
sns.set(style = "whitegrid")
plt.rcParams['font.sans-serif'] = 'SimHei'
os.chdir(r'D:\大学\泰迪销售项目\项目数据')
st=pd.read_csv('z.csv',encoding='gbk')
fig = plt.figure(figsize=(12, 6), dpi=80)
ax = fig.add_subplot(111)
ax.scatter(st['月份'],st['二级类'], s=st['数据'],color='green')
ax.set_xlabel('月份')
ax.set_ylabel('二级类')
plt.title('2017年C售货机交易额均值')
plt.savefig('2017年C售货机交易额均值.png')
plt.show()
