#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler

#資料讀取
path = './taxi_data/'
file = ['test_hire_stats.csv','train_gps_points.csv','train_hire_stats.csv']
"""
test_hire_stats.csv:乘車需求預測。
    
    Test_ID：    乘車需求之流水序號，共672筆
    Date：       預測日期，格式 YYYY-mm-dd，如2017-02-01
    Hour_slot：  預測時段，以一小時計，本欄位的值為0~23。
                 0代表0:00:00~0:59:59時段，1代表1:00:00~1:59:59，
                 依此類推，23代表23:00:00~23:59:59
    Hire_count： 內湖區該時段的乘車需求預測數量，本欄位下載時為空值，
                 請您填入您的預測值 (正整數值，0~n) 後上傳
                 
train_gps_points.csv:乘客上車GPS點位記錄，此資料乃經由篩選計程車錶於內湖區範圍內的啟動記錄而得，
                     並且將計程車錶啟動時間與地點視為乘客上車點，共4,118,812筆資料。
    
    Datetime：   計程車錶啟動時間 (台北時間 GMT+8:00)
    Longitude_X：GPS記錄經度 (WGS84座標)
    Latitude_Y： GPS記錄緯度 (WGS84座標)

train_hire_stats.csv
zones.csv
"""
#讀取test_hire_stats.csv
df1 = pd.read_csv(path+file[2])
#print(df1)


# In[7]:


#讀取train_gps_points.csv
#df2 = pd.read_csv(path+file[1])
#print(df2)


# In[8]:


#檢查有無遺失值，有就刪除
select_df = pd.DataFrame(df1)
drop_value = select_df.dropna()
#print(drop_value)


# In[ ]:

#X = df1.iloc[1:, 2:4].values

X = df1.iloc[:, 2:3].values
y = df1.iloc[:, 3].values


X = np.reshape(X, (-1, 1))
y = np.reshape(y, (-1, 1))
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)

#初始化SVR
regressor = SVR(kernel = 'rbf')


regressor.fit(X, y)

#y_pred = regressor.predict(sc_X.transform(np.array([[6.5]])))
#y_pred = sc_y.inverse_transform(y_pred)
y_pred = regressor.predict(6.5)


#plt.scatter(X, y, color = 'red')
#plt.plot(X, regressor.predict(X), color = 'blue')

#plt.title('Truth or Bluff (SVR)')
#plt.xlabel('Hour_slot(時段)')
#plt.ylabel('Hire_count(載客數)')
#plt.show()





