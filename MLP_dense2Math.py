import tensorflow as tf
import numpy as np
x_train=np.array([[3,5],[3,2]])
y_train=np.array([0,1])

model=tf.keras.models.Sequential([tf.keras.layers.Dense(1,activation=tf.nn.sigmoid,input_dim=2),
    tf.keras.layers.Dense(units=2,activation=tf.nn.sigmoid)
])

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.fit(x=x_train,y=y_train,epochs=3000)
model.summary()

score=model.evaluate(x_train,y_train)
print('score:',score)
predict=model.predict(x_train)
print('predict:',predict)
print('y_train',y_train[:])

weights,biases=model.layers[0].get_weights()
print(weights)
print(biases)
w000=weights[0][0]
w010=weights[1][0]
b00=biases[0]

print("--------")
weights1,biases1=model.layers[1].get_weights()
w100=weights1[0][0]
w110=weights1[0][1]
b10=biases1[0]
b11=biases1[1]
print(weights1)
print(biases1)
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
    y10=simoid_activation(y00*w100+b10)
    print(y10)
    y11=simoid_activation(y00*w110+b11)
    print(y11)

print('-----------------')
print(x_train[0])
outputdense2(x_train[0])
print(x_train[1])
outputdense2(x_train[1])