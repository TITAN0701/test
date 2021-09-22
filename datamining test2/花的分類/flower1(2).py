import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#headers =['date','plant-stand',' precip',' temp',' roots']
#arrhythmia = pd.read_excel('soybean-small.xlsx', names = headers)
arrhythmia = pd.read_excel('soybean-small.xlsx')
arrhythmia.columns = ['date','plant-stand','precip','temp','roots']

#x = arrhythmia[1:2]
#y = arrhythmia.target
#print('class lables : ', np.unique(y))

# 類別標籤  ---> 他沒有順序性 ， 並且分配數字給標籤
from sklearn.preprocessing import LabelEncoder
class_le =  LabelEncoder()
y = class_le.fit_transform(arrhythmia['roots'].values)
#class_le.inverse_transform(y)  對映的classlabel內容

#做one-hot encoding  將每一行資料列出，並指定單一行做數字轉換
from sklearn.preprocessing import OneHotEncoder
X = arrhythmia[['date','plant-stand','precip','temp','roots']].values
X[:, 4] = class_le.fit_transform(X[:, 4])

ohe = OneHotEncoder(categorical_features=[3])
ohe.fit_transform(X).toarray()  #轉成array

#更方便的 one-hot encoding
#pd.get_dummies(arrhythmia[['date','plant-stand','precip','temp','roots']])

#隨機劃分 訓練集與測試集  ---> 是預處理的關鍵
from sklearn.model_selection import train_test_split
#X, y = arrhythmia.iloc[:, 1:].values, arrhythmia.iloc[:, 0].values #列出原本一部分的資料
X_train, X_test, y_train, y_test =\
    train_test_split(X, y,test_size=0.3, random_state=1, stratify=y)
    
# 預處理 ， 正規化常見的作法有兩種  常態化or標準化  
# 最小最大縮放 (常態化)
from sklearn.preprocessing import MinMaxScaler
mms = MinMaxScaler()
X_train_norm = mms.fit_transform(X_train)
X_test_norm = mms.transform(X_test)
#標準化 z-score
from sklearn.preprocessing import StandardScaler
std = StandardScaler()
X_train_std = std.fit_transform(X_train)
X_test_std = std.transform(X_test)

#KNN演算法 --> 效率
#import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_std, y_train)
print('training accuracy : ', knn.score(X_train_std, y_train))
print('test accuracy : ', knn.score(X_test_std, y_test))


# 隨機森林  
from sklearn.ensemble import RandomForestClassifier

feat_labels = arrhythmia[1:]
forest = RandomForestClassifier(n_estimators=500, random_state=1)
forest.fit(X_train, y_train)

#是通過模型的feature_importances_方法獲取特徵貢獻度
#由於argsort排序是從小到大的，因此要用[::-1]進行倒序，得到從大到小的排序
#特徵重要度
features = list(arrhythmia)
importances = forest.feature_importances_
indices = np.argsort(importances)[::-1]
num_features = len(importances)

#將特徵重要度以柱狀圖展示
plt.figure()
plt.title("Feature importances")
plt.bar(range(num_features), importances[indices], color="g", align="center")
plt.xticks(range(num_features), [features[i] for i in indices], rotation='45')
plt.xlim([-1, num_features])
plt.show()

#輸出各個特徵的重要度
for i in indices:
    print ("{0} - {1:.3f}".format(features[i], importances[i]))
    
#主成分分析 (PCA)
# 特徵分解

#cov_mat = np.cov(X_train_std.T)     
#eigen_vals, eigen_vecs = np.linalg.eig(cov_mat)
#print('\n Eigenvalues \n%s' %eigen_vals)    
#tot = sum(eigen_vals)
#var_exp = [(i / tot) for i in
#            sorted(eigen_vals, reverse=True)]
#cum_var_exp = np.cumsum(var_exp)
#plt.bar(range(1,8), var_exp, alpha=0.5, align='center',
#        label='individual explained variance') 
#plt.step(range(1,8), cum_var_exp, where='mid',
#         label='cumulative explained variance') 
#plt.ylabel('Explained variance ratio')
#plt.xlabel('Principal component index') #主成分指數
#plt.legend(loc='best')
#plt.show()
    
    
#求共變異係數矩陣
cov_mat = np.cov(X_train_std.T)
print("共變異係數矩陣.shape=",cov_mat.shape)
print("共變異係數矩陣=",cov_mat)

#求共變異係數矩陣 的特徵向量及特徵值
eigen_vals, eigen_vecs = np.linalg.eig(cov_mat)
print("\n特徵向量.shape=",eigen_vecs.shape)
print("特徵向量=",eigen_vecs)
print("特徵值=",eigen_vals)

#計算解釋變異數比率 各特徵值/特徵值總和
tot = sum(eigen_vals)
var_exp = [(i / tot) for i in sorted(eigen_vals, reverse=True)]
cum_var_exp = np.cumsum(var_exp)
print("\n各特徵值變異數比率：",var_exp)
print("特徵值變異數比率累加：",cum_var_exp)








