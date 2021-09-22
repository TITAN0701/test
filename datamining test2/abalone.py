import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

headers = ['Sex','Length','Diameter','Height','Whole weight','Shucked weight',
           'Viscera weight','Shell weight','Rings']

abalone = pd.read_excel('abalone.xlsx',
                        names = headers)

#將性別轉成數字
abalone['Sex'] = abalone['Sex'].replace(['M','F','I'],[1,2,3])

#正規化數值類
#Sex = (abalone['Sex'] - abalone['Sex'].min())/(abalone['Sex'].max() - abalone['Sex'].min())
Length = (abalone['Length'] - abalone['Length'].min())/(abalone['Length'].max() - abalone['Length'].min())
Diameter = (abalone['Diameter'] - abalone['Diameter'].min())/(abalone['Diameter'].max() - abalone['Diameter'].min())
Height = (abalone['Height'] - abalone['Height'].min())/(abalone['Height'].max() - abalone['Height'].min())
Wholeweight = (abalone['Whole weight'] - abalone['Whole weight'].min())/(abalone['Whole weight'].max() - abalone['Whole weight'].min())
Shuckedweight = (abalone['Shucked weight'] - abalone['Shucked weight'].min())/(abalone['Shucked weight'].max() - abalone['Shucked weight'].min())
Visceraweight = (abalone['Viscera weight'] - abalone['Viscera weight'].min())/(abalone['Viscera weight'].max() - abalone['Viscera weight'].min())
Shellweight = (abalone['Shell weight'] - abalone['Shell weight'].min())/(abalone['Shell weight'].max() - abalone['Shell weight'].min())

#做class attribute的平均
Rings = abalone['Rings'].mean()

#設定區間，因為class attribute 是連續資料
def meanco(x,y):
    if x>y:
        return 1
    else:
        return 0
    
#加入區間使每 筆可以跑入呈現 1 和 0
abalone['Rings'] = abalone['Rings'].apply(lambda x:meanco(x,Rings))

#svm

#切割class attribute當作標籤
x = abalone.drop('Rings',axis=1)
y = abalone['Rings']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.20)

y_train = np.array(y_train, dtype=int)

svclassifier = SVC(kernel='linear')
#svclassifier = SVC(kernel='rdf')
#svclassifier = SVC(kernel='poly',degree=5)
#svclassifier = SVC(kernel='sigmoid')
svclassifier.fit(X_train, y_train)
#預測績效
y_pred = svclassifier.predict(X_test)
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))



