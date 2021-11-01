import numpy as np
import matplotlib.pyplot as plt

upper=5
lower=-5
num=100
def tanh_activation(x):
    return (2/(1+np.exp(-2*x)))-1
    
x_all=np.linspace(lower,upper,num=num)
vals=np.empty((0),int)
for x in x_all:
    y=tanh_activation(x)
    vals=np.append(vals,y)
    
plt.title('tanh')
plt.plot(x_all,vals,'g.')
plt.show()
