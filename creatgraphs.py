import matplotlib.pyplot as plt
import numpy as np 

import pylab
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
fontP = FontProperties()
fontP.set_size('small')
# comparisons 
# selection sort 
# y = [4950,499500,4.9995*10**7,4.99995*10**9] # selection sort [all]
# y1 = [4950,499500,4.9995*10**7,4.99995*10**9] # selection sort [all]
# y2 = [4950,499500,4.9995*10**7,4.99995*10**9] # selection sort [all]
# def fit(x,y):
# 	xfit = np.array(x)
# 	yfit= np.array(y)
# 	return np.polyfit(np.log(xfit), yfit, 1)


y = [1,1.66667,2.42857,3.26667,4.16129,5.09524,6.05512,7.03137,8.01761,9.00978,10.0054,11.0029]# Insertion sort [inc]
y1 = [1,1.66667,2.71429,3.73333,6.3871,7.66667,7.59055,9.06667,10.3033,12.2463,13.3972,14.0237] #insertion sort [rand]
y2 = [1,2,4,8,16,32,64,128,256,512,1024,2048] # insertion sort [dec]
# y = [99,999,9999,99999]# Bubble sort [inc]
# y1 = [4950,499500,4.9995*10**7,4.99995*10**9]# Bubble sort [random]
# y2 = [4872,499004,4.99862*10**7,4.99942*10**9]# Bubble sort [dec]
# y = [4950,499500,4.9995*10**7,4.9995*10**9]# Shell Sort [inc]
# y1 = [4950,499500,4.9995*10**7,4.9995*10**9]# Shell Sort [ran]
# y2 = [4950,499500,4.9995*10**7,4.9995*10**9]# Shell Sort [dec]

# runtime
# Selection sort 
# y = [1*10**-3 , 10, 1580, 158140 ] 
# y1 = [1*10**-3, 10, 1700, 155040]
# y2 = [1*10**-3, 10, 1570, 152340 ]

#Insertion sort 
# y = [5*10**-3 , 2*10**-5, 4*10**-3, .4 ] 
# y1 = [2*10**-4, .9, 1100, 81330]
# y2 = [1.5*10**-4, 10, 1610, 167550 ]

#Bubble sort 
# y = [1*10**-7 , 2*10**-5, 4*10**-3, .1 ] 
# y1 = [1*10**-3, 10, 950, 97770]
# y2 = [1*10**-3, 10, 1150, 115960]

#Shell sort 
# y = [3.9*10**-6, 4*10**-3, 10, 50 ] 
# y1 = [2*10**-5, 4.4*10**-4, .4, 50]
# y2 = [2*10**-5, 2.6*10**-4, .6, 60]

x = [1,3,7,15,31,63,127,255,511,1023,2047,4095]
x1 = [1,3,7,15,31,63,127,255,511,1023,2047,4095]
x2 = [1,3,7,15,31,63,127,255,511,1023,2047,4095]
# x1 = [1,2,3,4,5]
# y1 = [200,2000,20000,200000,2000000]
algorithm_name = 'BinaryTreeAssignment'
input_type = 'Increasing'
fig = plt.figure()
ax = fig.add_subplot(2, 1, 1)
plt.ylabel('average search cost')
plt.xlabel('input size (n)')
plt.title(algorithm_name + 'Sort' + '(' + input_type + ')')
# line, = ax.scatter(x,y color='blue', lw=2)
# plt.plot(x, y,'r-o',x1, y1,'c-*',x2, y2,'b-^', linewidth=1,alpha=.8)
# coefficients = fit(x,y)
# xfit = np.linspace(0,4095)
# yfit = coefficients[0] * log(np.linspace(0,4095)) + coefficients[1]
# plt.plot(fit,yfit)
plt.plot(x, y,'g-o')
# plt.plot(x2, y2,'b-o')

# plt.plot(x1,y1,'-o')
# plt.scatter(x,y)
# ax.set_xscale('log')
# ax.set_yscale('log')
# for i, txt in enumerate(y):
#     ax.annotate(txt, (x[i], y[i]))
# for i, txt in enumerate(y1):
#     ax.annotate(txt, (x[i], y1[i]))
# for i, txt in enumerate(y2):
#     ax.annotate(txt, (x[i], y2[i]))

ax.legend(['Perfect', 'Random', 'Linear'],prop=fontP,loc=0)
plt.show()
fig.savefig(algorithm_name + '_' + input_type+'runtime.png')



# [4950,499500,4.9995**7,4.99995**9]