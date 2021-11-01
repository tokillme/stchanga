import numpy as np
import matplotlib.pyplot as plt

upper=5
lower=-5
num=100
# 0 for x<0 , x for x>=0
def relu_activation(x):
    if x<0:
        return 0
    return x

x_all=np.linspace(lower,upper,num=num)
vals=np.empty((0),int) #numpy.ndarray

for x in x_all:
    y=relu_activation(x)
    vals=np.append(vals,y)

plt.title('Relu')
plt.plot(x_all,vals,'r.')
plt.show()