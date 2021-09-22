import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np

Concrete = pd.read_csv('Concrete_Data.csv')

#資料清洗
#Concrete.replace(' ?',np.nan, inplace = True)
train_x=Concrete.dropna()
#train_set=pd.get_dummies(Concrete)
#Concrete.head()

#正規化
Cement = (Concrete['Cement'] - Concrete['Cement'].min())/(Concrete['Cement'].max() - Concrete['Cement'].min())
BlastFurnaceSlag = (Concrete['Blast Furnace Slag'] - Concrete['Blast Furnace Slag'].min())/(Concrete['Blast Furnace Slag'].max() - Concrete['Blast Furnace Slag'].min())
FlyAsh = (Concrete['Fly Ash'] - Concrete['Fly Ash'].min())/(Concrete['Fly Ash'].max() - Concrete['Fly Ash'].min())
Water = (Concrete['Water'] - Concrete['Water'].min())/(Concrete['Water'].max() - Concrete['Water'].min())
Superplasticizer = (Concrete['Superplasticizer'] - Concrete['Superplasticizer'].min())/(Concrete['Superplasticizer'].max() - Concrete['Superplasticizer'].min())
CoarseAggregate = (Concrete['Coarse Aggregate'] - Concrete['Coarse Aggregate'].min())/(Concrete['Coarse Aggregate'].max() - Concrete['Coarse Aggregate'].min())
FineAggregate = (Concrete['Fine Aggregate'] - Concrete['Fine Aggregate'].min())/(Concrete['Fine Aggregate'].max() - Concrete['Fine Aggregate'].min())
Age = (Concrete['Age'] - Concrete['Age'].min())/(Concrete['Age'].max() - Concrete['Age'].min())

#設定區間，因為class attribute 是連續資料
def meanco(x,y):
    if x>y:
        return 1
    else:
        return 0

#設定class attribute 的平均值
#加入區間使每 筆可以跑入呈現 1 和 0
Concretecompressivestrength = Concrete['Concrete compressive strength'].mean()
Concrete['Concrete compressive strength'] = Concrete['Concrete compressive strength'].apply(lambda x:meanco(x,Concretecompressivestrength))

#Concrete.head()
#Concrete.shape

#svm

#切割class attribute當作標籤
x=Concrete.drop('Concrete compressive strength',axis=1)
y=Concrete['Concrete compressive strength']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.20)

y_train = np.array(y_train, dtype=int)


#svclassifier = SVC(kernel='linear')
#svclassifier = SVC(kernel='rdf')
#svclassifier = SVC(kernel='poly',degree=5)
svclassifier = SVC(kernel='sigmoid')
svclassifier.fit(X_train, y_train)
#預測績效
y_pred = svclassifier.predict(X_test)
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

#Blast Furnace Slag,Fly Ash,Water,
#Superplasticizer,Coarse Aggregate,Fine Aggregate,Age

##所有Fare的算術平均數
#mu=data_sample.mean()
##標準差
#std=data_sample.std()
#標準化後之結果
#z_score_normalized = (data_sample - mu) / std
#print(z_score_normalized)

#z-score 函式
#def z_score_normalization(df, cols):
#    train_set_normalized = train_set.copy()
#    for col in cols:
#        all_col_data = train_set_normalized[col].copy()
##        print(all_col_data)
#        mu = all_col_data.mean()
#        std = all_col_data.std()
#        
#        z_score_normalized = (all_col_data - mu) / std
#        train_set_normalized[col] = z_score_normalized
#    return train_set_normalized
    
#normalized = pd.DataFrame(z_score_normalization(train_set, 
#                                                train_set.keys()))
#scale = StandardScaler() #z-scaler物件
#train_set_scaled = pd.DataFrame(scale.fit_transform(train_set),
#                                columns=train_set.keys())

##查看每一筆的資料正規化後的績效
#data_sample.hist(figsize=(20,20))
#plt.show()
#
##describe方法更加明顯(各個表徵的min、max值差異極大)
#data_sample.describe()
#
##觀察訓練集的缺值
#print(data_sample.isnull().sum())

#將屬性標籤分開
#X=data_sample.drop('Water  (component 4)(kg in a m^3 mixture)', axis=1)
#y=data_sample['Fly Ash (component 3)(kg in a m^3 mixture)']

#train_x, X_test, train_y, y_test = train_test_split(
#    X, y, test_size=0.20, random_state=1, stratify=y)
#
#scale.fit(train_x)
#X_train_std = scale.fit_transform(train_x)
#X_test_std = scale.transform(X_test)
#svm = SVC(gamma=0.1, C=1,kernel='linear')
#svm.fit(X_train_std, train_y)
#print('SVM')
#print("Training set score: %f" % svm.score(X_train_std, train_y))
#print("Test set score: %f" % svm.score(X_test_std, y_test))


