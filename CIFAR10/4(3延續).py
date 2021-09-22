import os
import numpy as np
import pandas as pd
import tensorflow as tf

from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras import layers
from keras import models
from keras.callbacks import EarlyStopping

cifar10_train = 'C:/Users/abc86/Desktop/manchine learning/CIFAR10/train/'
cifar10_test = 'C:/Users/abc86/Desktop/manchine learning/CIFAR10/test/'
#cifar10_train_dirs = os.listdir(cifar10_train)
#for file in cifar10_train_dirs:
#    if os.path.isdir(os.path.join(cifar10_train, file)):
#        print('directory:'+file)
# walk的方式則會將指定路徑底下所有的目錄與檔案都列出來(包含子目錄以及子目錄底下的檔案)
#cifar10_train_lisdir =os.walk(cifar10_train)
#cifar10_test_lisdir =os.walk(cifar10_test)

#train = []
#for root, dirs,train_files in cifar10_train_lisdir:
#    for file in train_files:
#        if os.path.splitext(file)[1] == '.png':
#            train.append(os.path.join(root,file))
#            
#test = []
#for root, dirs,test_files in cifar10_test_lisdir:
#    for file in test_files:
#        if os.path.splitext(file)[1] == '.png':
#            test.append(os.path.join(root,file))
train_data = ImageDataGenerator(rescale=1./255) #1./255壓縮至0,1
test_data = ImageDataGenerator(rescale=1./255)  #1./255壓縮至0,1

train_generator = train_data.flow_from_directory(
        cifar10_train,
        target_size=(28, 28),
        batch_size = 50000,
        class_mode='categorical')
test_generator = test_data.flow_from_directory(
        cifar10_test,
        target_size= (28, 28),
        batch_size = 10000,
        class_mode='categorical')

model=models.Sequential()
early_stopping = EarlyStopping(monitor='val_accuracy', mode = "max",patience=200,restore_best_weights=True)

model.add(layers.Conv2D(32,(3,3), padding='same',activation='relu',input_shape=(28,28,3)))
model.add(layers.Conv2D(32,(3,3),activation='relu'))
model.add(layers.Dropout(0.25))
 
model.add(layers.Conv2D(64,(3,3), padding='same',activation='relu'))
model.add(layers.Conv2D(64,(3,3), activation='relu'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Dropout(0.25))
 
model.add(layers.Conv2D(128,(3,3), padding='same',activation='relu'))
model.add(layers.Conv2D(128,(3,3), activation='relu'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Dropout(0.25))
 
model.add(layers.Conv2D(256,(3,3), padding='same',activation='relu'))
model.add(layers.Conv2D(256,(3,3), activation='relu'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Dropout(0.25))
 
model.add(layers.Flatten())
model.add(layers.Dense(1024,activation='relu'))
model.add(layers.Dropout(0.5))

model.add(layers.Dense(10,activation='softmax'))

#計算資料的 batch shape
for data_batch, labels_batch in train_generator:
    print('data batch shape:',data_batch.shape)
    print('labels batch shape:',labels_batch.shape)
    break 

for data_batch2, labels_batch2 in test_generator:
    print('data batch shape:',data_batch2.shape)
    print('labels batch shape:',labels_batch2.shape)
    break 

model.compile(optimizer='Adam' , loss='categorical_crossentropy' , metrics=['accuracy'])
model.fit(data_batch, labels_batch, epochs=200, batch_size=64,
          verbose=1,validation_split=0.10,callbacks=[early_stopping])

loss, accuracy = model.evaluate(data_batch2, labels_batch2)
print('Test:')
print('Loss:', loss)
print('Accuracy:', accuracy)