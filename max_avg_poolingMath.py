import cv2
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

s=5 #5*5
img=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
print(img)

model=tf.keras.models.Sequential()
model.add(tf.keras.layers.MaxPool2D(pool_size=(2,2),input_shape=(s,s,1)))
model.summary()

mode2=tf.keras.models.Sequential()
mode2.add(tf.keras.layers.AveragePooling2D(pool_size=(2,2),input_shape=(s,s,1)))
mode2.summary()

def visualize_img(i_model,i_img,i_subplot):
    i_img=np.reshape(i_img,(1,s,s,1)) #改變維度
    print(i_img)
    img=i_model.predict(i_img) #取得Conv2D
    img=np.reshape(img,(img.shape[1],img.shape[2])) #改變維度img=1 img.shape圖片邊長
    plt.subplot(i_subplot)
    plt.imshow(img,cmap='gray') #顯示圖片
    print(img)
visualize_img(model,img,121)
visualize_img(mode2,img,122)
plt.show()
