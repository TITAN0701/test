# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 17:15:22 2019

@author: -
"""

import os
train = []
y=[]
names =os.listdir('C:/Users/user/Desktop/mini_newsgroups') #得到文件下名稱
for name in names:
    path = 'C:/Users/user/Desktop/mini_newsgroups/'+ name
    files= os.listdir(path) 
    for file in files: 
         if not os.path.isdir(file): 
              f = open(path+"/"+file,encoding='cp1252'); 
              iter_f = iter(f); 
              str = ""
              for line in iter_f: 
                  str = str + line
              y.append(name)
              train.append(str)
    print(train) 
    print(y)
    
