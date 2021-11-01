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

weights,biases=model.layers[1].get_weights()
print(weights)
print(biases)