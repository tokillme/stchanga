import numpy as np
import matplotlib.pyplot as plt

upper=5
lower=-5
num=100

def sigmoid_activation(x):
	return 1/(1+np.exp(-x))
	
x_all=np.linspace(lower,upper,num=num)
vals=np.empty((0),int) #空[]

for x in x_all:
	y=sigmoid_activation(x)
	vals=np.append(vals,y)
	
plt.title('Sigmoid')
plt.plot(x_all,vals,'b.')
plt.show()