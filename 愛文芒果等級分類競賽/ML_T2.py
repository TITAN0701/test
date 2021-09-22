# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 23:20:57 2020

@author: Thomas
"""

# import os
# import tensorflow as tf
# if tf.test.gpu_device_name():
#     print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))
# else:
#     print("Please install GPU version of TF")
#GPU is died , cant hold max memory
# import tensorflow as tf
# gpus = tf.config.experimental.list_physical_devices('GPU')
# tf.config.experimental.set_virtual_device_configuration(
#     gpus[0],
#     [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=8192)])
#%%前處理

from keras.preprocessing.image import ImageDataGenerator

train_data = ImageDataGenerator(rescale=1./255) #1./255壓縮至0,1
test_data = ImageDataGenerator(rescale=1./255)  #1./255壓縮至0,1

train_dir = 'C:/Users/Thomas/Desktop/ML2/CIFAR10/train/'
test_dir = 'C:/Users/Thomas/Desktop/ML2/CIFAR10/test/'


train_generator = train_data.flow_from_directory(
        train_dir,
        target_size=(28, 28),
        batch_size = 50000,
        class_mode='categorical')
test_generator = test_data.flow_from_directory(
        test_dir,
        target_size= (28, 28),
        batch_size = 10000,
        class_mode='categorical')
#%%
for data_batch, labels_batch in train_generator:
    print('data batch shape:',data_batch.shape)
    print('labels batch shape:',labels_batch.shape)
    break 

for data_batch2, labels_batch2 in test_generator:
    print('data batch shape:',data_batch2.shape)
    print('labels batch shape:',labels_batch2.shape)
    break 

#%%
# from keras import backend as K
# from keras.layers import Layer
# from keras.metrics import categorical_accuracy

# import tensorflow as tf
# import math as m

# class ArcFace(Layer):
#     '''Custom Keras layer implementing ArcFace including:
#     1. Generation of embeddings
#     2. Loss function
#     3. Accuracy function
#     '''

#     def __init__(self, output_dim, class_num, margin=0.5, scale=64., **kwargs):
#         self.output_dim = output_dim
#         self.class_num = class_num
#         self.margin = margin
#         self.s = scale

#         self.cos_m = tf.math.cos(margin)
#         self.sin_m = tf.math.sin(margin)
#         self.mm = self.sin_m * margin
#         self.threshold = tf.math.cos(tf.constant(m.pi) - margin)
#         super(ArcFace, self).__init__(**kwargs)


#     def build(self, input_shape):
#         # Create a trainable weight variable for this layer.
#         self.kernel = self.add_weight(name='kernel', 
#                                       shape=(input_shape[1], self.class_num),
#                                       initializer='glorot_normal',
#                                       trainable=True)
#         super(ArcFace, self).build(input_shape)  # Be sure to call this at the end


#     def call(self, x):
#         embeddings = tf.nn.l2_normalize(x, axis=1, name='normed_embeddings')
#         weights = tf.nn.l2_normalize(self.kernel, axis=0, name='normed_weights')
#         cos_t = tf.matmul(embeddings, weights, name='cos_t')
#         return cos_t


#     def get_logits(self, labels, y_pred):
#         cos_t = y_pred
#         cos_t2 = tf.square(cos_t, name='cos_2')
#         sin_t2 = tf.subtract(1., cos_t2, name='sin_2')
#         sin_t = tf.sqrt(sin_t2, name='sin_t')
#         cos_mt = self.s * tf.subtract(tf.multiply(cos_t, self.cos_m), tf.multiply(sin_t, self.sin_m), name='cos_mt')
#         cond_v = cos_t - self.threshold
#         cond = tf.cast(tf.nn.relu(cond_v, name='if_else'), dtype=tf.bool)
#         keep_val = self.s*(cos_t - self.mm)
#         cos_mt_temp = tf.where(cond, cos_mt, keep_val)
#         mask = tf.one_hot(labels, depth=self.class_num, name='one_hot_mask')
#         inv_mask = tf.subtract(1., mask, name='inverse_mask')
#         s_cos_t = tf.multiply(self.s, cos_t, name='scalar_cos_t')
#         output = tf.add(tf.multiply(s_cos_t, inv_mask), tf.multiply(cos_mt_temp, mask), name='arcface_logits')
#         return output


#     def loss(self, y_true, y_pred):
#         labels = K.argmax(y_true, axis=-1)
#         logits = self.get_logits(labels, y_pred)
#         loss = tf.losses.sparse_categorical_crossentropy(labels,logits)
#         return loss


#     def accuracy(self, y_true, y_pred):
#         labels = K.argmax(y_true, axis=-1)
#         logits = self.get_logits(labels, y_pred)
#         accuracy = categorical_accuracy(y_true=labels, y_pred=logits)
#         return accuracy
    

#     def compute_output_shape(self, input_shape):
#         return (input_shape[0], self.output_dim)

#%%
from keras import layers
from keras import models
import tensorflow as tf
from keras.callbacks import EarlyStopping

#進行CNN模型的建構
model=models.Sequential()
early_stopping = EarlyStopping(monitor='val_accuracy', mode = "max",patience=200,restore_best_weights=True)
# model.add(layers.Conv2D(32,(3,3),activation='relu',input_shape=(28,28,3)))
# model.add(layers.MaxPooling2D((2,2)))
# model.add(layers.Conv2D(64,(3,3),activation='relu'))
# model.add(layers.MaxPooling2D((2,2)))
# model.add(layers.Dropout(0.5))
# model.add(layers.Conv2D(64,(3,3),activation='relu'))

# model.add(layers.Flatten())
# model.add(layers.Dense(64,activation='relu'))
# model.add(layers.Dense(10,activation='softmax'))

# model.compile(optimizer='Adam' , loss='categorical_crossentropy' , metrics=['accuracy'])
# model.fit(data_batch, labels_batch, epochs=1000000000, batch_size=64,
#           verbose=1,validation_split=0.10,callbacks=[early_stopping])

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
# model.add(ArcFace(10,10,0.3))
# model.add(ArcFace(n_classes=10))
model.add(layers.Dense(10,activation='softmax'))


model.compile(optimizer='Adam' , loss='categorical_crossentropy' , metrics=['accuracy'])
model.fit(data_batch, labels_batch, epochs=1000000000, batch_size=64,
          verbose=1,validation_split=0.10,callbacks=[early_stopping])


# history = model.fit_generator(
#     train_generator,
#     steps_per_epoch=1000,
#     epochs=1,
#     validation_data = test_generator,
#     validation_steps = 50)

# model.save('model_test_01.h5')

#%%
loss, accuracy = model.evaluate(data_batch2, labels_batch2)
print('Test:')
print('Loss:', loss)
print('Accuracy:', accuracy)


