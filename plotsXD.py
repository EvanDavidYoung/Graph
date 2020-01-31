import matplotlib.pyplot as plt


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

y = [99,999,9999,99999]# Insertion sort [inc]
y1 = [2607,252953,2.48595*10**7,2.48595*10**9] #insertion sort [rand]
y2 = [4950,499500,4.9995*10**7,4.99995*10**9] # insertion sort [dec]
# y = [99,999,9999,99999]# Bubble sort [inc]
# y1 = [4950,499500,4.9995*10**7,4.99995*10**9]# Bubble sort [random]
# y2 = [4872,499004,4.99862*10**7,4.99942*10**9]# Bubble sort [dec]
# y = [4950,499500,4.9995*10**7,4.9995*10**9]# Shell Sort [inc]
# y1 = [4950,499500,4.9995*10**7,4.9995*10**9]# Shell Sort [ran]
# y2 = [4950,499500,4.9995*10**7,4.9995*10**9]# Shell Sort [dec]

# runtime
# Selection sort 
# y0 = [1*10**-3 , 10, 1580, 158140 ] 
# y0 = [1*10**-3, 10, 1700, 155040]
y0 = [1*10**-3, 10, 1570, 152340 ]

#Insertion sort 
# y1 = [5*10**-3 , 2*10**-5, 4*10**-3, .4 ] 
# y1 = [2*10**-4, .9, 1100, 81330]
y1 = [1.5*10**-4, 10, 1610, 167550 ]

#Bubble sort 
# y2 = [1*10**-7 , 2*10**-5, 4*10**-3, .1 ] 
# y2 = [1*10**-3, 10, 950, 97770]
y2 = [1*10**-3, 10, 1150, 115960]

#Shell sort 
# y3 = [2*10**-5, 3*10**-3, .2, 50 ] 
# y3 = [2*10**-5, 3*10**-3, 10, 80]
y3 = [3*10**-5, 5*10**-3, .6, 70]
#Radix sort 
# y4 = [3.9*10**-6, 4*10**-3, 10, 50 ] 
# y4 = [2*10**-5, 4.4*10**-4, .4, 50]
y4 = [2*10**-5, 2.6*10**-4, .6, 60]

x = [100,1000,10000,100000]
x1 = [100,1000,10000,100000]
x2 = [100,1000,10000,100000]
# x1 = [1,2,3,4,5]
# y1 = [200,2000,20000,200000,2000000]
title = 'Selection,Insertion,Bubble,Shell,Radix'
input_type = 'Decreasing'
fig = plt.figure()
ax = fig.add_subplot(2, 1, 1)

ylabel = "YLABEL"
xlabel = "XLABEL"
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.title(title + 'Sort' + '(' + input_type + ')')
# line, = ax.scatter(x,y color='blue', lw=2)
plt.plot(x, y0,'r-o',x, y1,'c-*',x, y2,'b-^',x,y3,'m-H',x,y4,'g-+', linewidth=1,alpha=.8)
# plt.plot(x1, y1,'g-o')
# plt.plot(x2, y2,'b-o')

# plt.plot(x1,y1,'-o')
# plt.scatter(x,y)
ax.set_xscale('log')
ax.set_yscale('log')
# for i, txt in enumerate(y):
#     ax.annotate(txt, (x[i], y[i]))
# for i, txt in enumerate(y1):
#     ax.annotate(txt, (x[i], y1[i]))
# for i, txt in enumerate(y2):
#     ax.annotate(txt, (x[i], y2[i]))

ax.legend(['Selection', 'Insertion', 'Bubble', 'Shell','Radix'],prop=fontP,loc=0)
plt.show()
fig.savefig(title + '_' + input_type+'runtime.png')



# [4950,499500,4.9995**7,4.99995**9]