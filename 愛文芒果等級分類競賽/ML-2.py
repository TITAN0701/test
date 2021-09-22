# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 09:55:14 2020

@author: 88697
"""

from keras import models
from keras import layers
from keras import optimizers
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from keras.utils import to_categorical
import pandas as pd
import numpy as np
from keras.datasets import mnist
from keras.layers.normalization import BatchNormalization


data = pd.read_csv("adult.data.csv")
data.shape
data.head()
data.replace(" ?",np.nan,inplace = True)
df = data.dropna()
df.columns = ['age','workclass','fnlwgt','education',
             'education-num','marital-status','occupation',
             'relationship','race','sex','capital-gain',
             'capital-loss','hours-per-week','native-country','income']

#onehot-encoding
#工作類型
pd.get_dummies(df['workclass'])
workclass_encoding = pd.get_dummies(df['workclass'], prefix = 'workclass')
df = df.drop('workclass', 1)
#學位
pd.get_dummies(df['education'])
education_encoding = pd.get_dummies(df['education'], prefix = 'education')
df = df.drop('education', 1)
#婚姻
pd.get_dummies(df['marital-status'])
marital_status_encoding = pd.get_dummies(df['marital-status'], prefix = 'marital-status')
df = df.drop('marital-status', 1)
#職業
pd.get_dummies(df['occupation'])
occupation_encoding = pd.get_dummies(df['occupation'], prefix = 'occupation')
df = df.drop('occupation', 1)
#關係
pd.get_dummies(df['relationship'])
relationship_encoding = pd.get_dummies(df['relationship'], prefix = 'relationship')
df = df.drop('relationship', 1)
#種族
pd.get_dummies(df['race'])
race_encoding = pd.get_dummies(df['race'], prefix = 'race')
df = df.drop('race', 1)
#性別
pd.get_dummies(df['sex'])
sex_encoding = pd.get_dummies(df['sex'], prefix = 'sex')
df = df.drop('sex', 1)
#國家
pd.get_dummies(df['native-country'])
native_country_encoding = pd.get_dummies(df['native-country'], prefix = 'native-country')
df = df.drop('native-country', 1)
#結合
df2 = pd.concat([workclass_encoding,education_encoding,marital_status_encoding,
           occupation_encoding,relationship_encoding,race_encoding,
           sex_encoding,native_country_encoding,df],axis=1)
#正規化
#年齡正規
df2['age'] = (df2['age'] - df2['age'].min())/(df2['age'].max() - df2['age'].min())
#週工作時間正規
df2['hours-per-week'] = (df2['hours-per-week'] - df2['hours-per-week'].min())/(df2['hours-per-week'].max() - df2['hours-per-week'].min())
#fnlwgt
df2['fnlwgt'] = (df2['fnlwgt'] - df2['fnlwgt'].min())/(df2['fnlwgt'].max() - df2['fnlwgt'].min())
#edu-num
df2['education-num'] = (df2['education-num'] - df2['education-num'].min())/(df2['education-num'].max() - df2['education-num'].min())
#capital-gain
df2['capital-gain'] = (df2['capital-gain'] - df2['capital-gain'].min())/(df2['capital-gain'].max() - df2['capital-gain'].min())
#capital-loss
df2['capital-loss'] = (df2['capital-loss'] - df2['capital-loss'].min())/(df2['capital-loss'].max() - df2['capital-loss'].min())

salary_map={' <=50K':1,' >50K':0}
df2['income']=df2['income'].map(salary_map).astype(int)

#income
pd.get_dummies(df['income'])
income_encoding = pd.get_dummies(df['income'], prefix = 'income')
df = df.drop('income', 1)

#%%
data2 = pd.read_csv("adult.test.csv")
data2.shape
data2.head()
data2.replace(" ?",np.nan,inplace = True)
df3 = data2.dropna()
df3.columns = ['age','workclass','fnlwgt','education',
             'education-num','marital-status','occupation',
             'relationship','race','sex','capital-gain',
             'capital-loss','hours-per-week','native-country','income']
#%%
#onehot-encoding
#工作類型
pd.get_dummies(df3['workclass'])
bworkclass_encoding = pd.get_dummies(df3['workclass'], prefix = 'workclass')
df3 = df3.drop('workclass', 1)
#學位
pd.get_dummies(df3['education'])
beducation_encoding = pd.get_dummies(df3['education'], prefix = 'education')
df3 = df3.drop('education', 1)
#婚姻
pd.get_dummies(df3['marital-status'])
bmarital_status_encoding = pd.get_dummies(df3['marital-status'], prefix = 'marital-status')
df3 = df3.drop('marital-status', 1)
#職業
pd.get_dummies(df3['occupation'])
boccupation_encoding = pd.get_dummies(df3['occupation'], prefix = 'occupation')
df3 = df3.drop('occupation', 1)
#關係
pd.get_dummies(df3['relationship'])
brelationship_encoding = pd.get_dummies(df3['relationship'], prefix = 'relationship')
df3 = df3.drop('relationship', 1)
#種族
pd.get_dummies(df3['race'])
brace_encoding = pd.get_dummies(df3['race'], prefix = 'race')
df3 = df3.drop('race', 1)
#性別
pd.get_dummies(df3['sex'])
bsex_encoding = pd.get_dummies(df3['sex'], prefix = 'sex')
df3 = df3.drop('sex', 1)
#國家
pd.get_dummies(df3['native-country'])
bnative_country_encoding = pd.get_dummies(df3['native-country'], prefix = 'native-country')
df3 = df3.drop('native-country', 1)
#結合
df4 = pd.concat([bworkclass_encoding,beducation_encoding,bmarital_status_encoding,
           boccupation_encoding,brelationship_encoding,brace_encoding,
           bsex_encoding,bnative_country_encoding,df3],axis=1)
#正規化
#年齡正規
df4['age'] = (df4['age'] - df4['age'].min())/(df4['age'].max() - df4['age'].min())
#週工作時間正規
df4['hours-per-week'] = (df4['hours-per-week'] - df4['hours-per-week'].min())/(df4['hours-per-week'].max() - df4['hours-per-week'].min())
#fnlwgt
df4['fnlwgt'] = (df4['fnlwgt'] - df4['fnlwgt'].min())/(df4['fnlwgt'].max() - df4['fnlwgt'].min())
#edu-num
df4['education-num'] = (df4['education-num'] - df4['education-num'].min())/(df4['education-num'].max() - df4['education-num'].min())
#capital-gain
df4['capital-gain'] = (df4['capital-gain'] - df4['capital-gain'].min())/(df4['capital-gain'].max() - df4['capital-gain'].min())
#capital-loss
df4['capital-loss'] = (df4['capital-loss'] - df4['capital-loss'].min())/(df4['capital-loss'].max() - df4['capital-loss'].min())

bsalary_map={' <=50K.':1,' >50K.':0}
df4['income']=df4['income'].map(bsalary_map).astype(int)
#income
pd.get_dummies(df3['income'])
bincome_encoding = pd.get_dummies(df3['income'], prefix = 'income')
df3 = df3.drop('income', 1)

#%% 類別預測

X = df2.drop('income', axis=1)
Y = income_encoding
XX = df4.drop('income', axis=1)
YY = bincome_encoding


X_train, X_valid, Y_train, Y_valid = train_test_split(X, Y, XX, YY) 
print(X_train.shape) 
print(X_valid.shape) 
print(Y_train.shape) 
print(Y_valid.shape)  
#%%
model = models.Sequential()
model.add(layers.Dense(32, activation='relu', input_dim=108))
model.add(BatchNormalization())
# model.add(layers.Dense(32, activation='relu'))
# model.add(BatchNormalization())
model.add(layers.Dense(16, activation='relu'))
model.add(BatchNormalization())
# model.add(layers.Dense(8, activation='relu'))
# model.add(BatchNormalization())
model.add(layers.Dense(4, activation='relu'))
model.add(BatchNormalization())
model.add(layers.Dense(2, activation='softmax'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, Y_train, epochs=20, batch_size=128)

results = model.evaluate(X_valid, Y_valid)
print(results)

#%%

X = df2['hours-per-week']
