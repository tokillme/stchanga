import tensorflow as tf
import numpy as np
x_train=np.array([[3,5],[3,2]])
y_train=np.array([0,1])

model=tf.keras.models.Sequential([tf.keras.layers.Dense(1,activation=tf.nn.sigmoid,input_dim=2)])

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
model.fit(x=x_train,y=y_train,epochs=3000)
model.summary()

score=model.evaluate(x_train,y_train)
print('score:',score)
predict=model.predict(x_train)
print('predict:',predict)
print('y_train',y_train[:])

weights,biases=model.layers[0].get_weights()
w000=weights[0][0]
w010=weights[1][0]
b00=biases[0]

print("--------")
upper=5
lower=-5
num=100
def simoid_activation(x):
    return 1/(1+np.exp(-x))

def outputdense2(inputValue):
    x0=inputValue[0]
    x1=inputValue[1]
    y00=simoid_activation(x0*w000+x1*w010+b00)
    print(y00)

print('-----------------')
print(x_train[0])
outputdense2(x_train[0])
print(x_train[1])
outputdense2(x_train[1])