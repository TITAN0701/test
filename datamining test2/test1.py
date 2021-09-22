import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from pydotplus import graph_from_dot_data
from mlxtend.plotting import plot_decision_regions
from sklearn.svm import SVC
from matplotlib.colors import ListedColormap
from numpy import nan as NA
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.manifold import Isomap

#訓練集
train_set_card = pd.read_excel('C:\\Users\\abc86\\Desktop\\(DM)Datamaining\\作業二\\default of credit card clients2.xlsx', index_col=0)
train_set=train_set_card.dropna()
train_set=train_set_card.fillna(0)
train_set=pd.get_dummies(train_set)
data_sample=train_set.head()

#測試集
test_set_card = pd.read_excel('C:\\Users\\abc86\\Desktop\\(DM)Datamaining\\作業二\\default of credit card clients2.xlsx', index_col=0)

#所有Fare的算術平均數
mu=data_sample.mean()
#標準差
std=data_sample.std()
#標準化後之結果
z_score_normalized = (data_sample - mu) / std
#print(z_score_normalized)

#z-score 函式
def z_score_normalization(df, cols):
    train_set_normalized = train_set.copy()
    for col in cols:
        all_col_data = train_set_normalized[col].copy()
#        print(all_col_data)
        mu = all_col_data.mean()
        std = all_col_data.std()
        
        z_score_normalized = (all_col_data - mu) / std
        train_set_normalized[col] = z_score_normalized
    return train_set_normalized
    
normalized = pd.DataFrame(z_score_normalization(train_set, 
                                                train_set.keys()))
scale = StandardScaler() #z-scaler物件
train_set_scaled = pd.DataFrame(scale.fit_transform(train_set),
                                columns=train_set.keys())

#查看每一筆的資料正規化後的績效
train_set_card.hist(figsize=(30,30))
#plt.show()

#describe方法更加明顯(各個表徵的min、max值差異極大)
#train_set_card.describe()

#觀察訓練集的缺值
#print(train_set.isnull().sum())
#結果是無缺值

#將屬性標籤分開
X=train_set.drop('default payment next month', axis=1)
y=train_set['default payment next month']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=1, stratify=y)
    

scale = StandardScaler()
scale.fit(X_train)
X_train_std = scale.fit_transform(X_train)
X_test_std = scale.transform(X_test)

svm = SVC(gamma=0.1, C=1,kernel='poly', degree=10)
svm.fit(X_train_std, y_train)
print('SVM')
print("Training set score: %f" % svm.score(X_train_std, y_train))
print("Test set score: %f" % svm.score(X_test_std, y_test))

# 對 `digits` 資料降維
X_iso = Isomap(n_neighbors=100).fit_transform(X_train)
# 使用 SVC 演算法
predicted = svm.predict(X_train)

# 在 1x2 的網格上繪製子圖形
fig, ax = plt.subplots(1, 2, figsize=(8, 4))

# 調整外觀
fig.subplots_adjust(top=0.75)

# 繪製散佈圖 
ax[0].scatter(X_iso[:, 0], X_iso[:, 1], c=predicted)
ax[0].set_title('Predicted labels')
ax[1].scatter(X_iso[:, 0], X_iso[:, 1], c=y_train)
ax[1].set_title('Actual Labels')

# 加入標題
fig.suptitle('Predicted versus actual labels', fontsize=14, fontweight='bold')

# 顯示圖形
#plt.show()