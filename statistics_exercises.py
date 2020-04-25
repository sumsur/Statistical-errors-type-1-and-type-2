import matplotlib.pyplot as plt
import scipy.stats
import numpy as np


x_min = 0.0
x_max = 16.0
x_min1 = 1.0
x_max1 = 20.0

mean = 8.0 
mean1 = 10.0
std = 2.0
std1= 2.0

x = np.linspace(x_min, x_max, 100)
x1= np.linspace(x_min1, x_max1, 100)

y = scipy.stats.norm.pdf(x,mean,std)
y1 = scipy.stats.norm.pdf(x1,mean1,std1)

plt.plot(x,y, color='coral')
plt.plot(x1, y1, color='green')

#----------------------------------------------------------------------------------------#
# fill error type 1

pt1 = mean1 + 1.25*std1
x_pos=14.5
y_pos=0.05
plt.text(x_pos, y_pos, "Error type 1")
plt.plot([pt1 ,pt1 ],[0.0,scipy.stats.norm.pdf(pt1 ,mean1, std1)], color='black')

pt2 = mean1 + 3.5 * std1
plt.plot([pt2 ,pt2 ],[0.0,scipy.stats.norm.pdf(pt2 ,mean1, std1)], color='black')

ptx = np.linspace(pt1, pt2, 10)
pty = scipy.stats.norm.pdf(ptx,mean1,std1)

plt.fill_between(ptx, pty, color='yellow', alpha=1.0)

#----------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------#
# fill error type 2

pt1 = mean1 - 2.5 * std1
x_pos=2.5
y_pos=0.03
plt.text(x_pos, y_pos, "Error type 2")
plt.plot([pt1 ,pt1 ],[0.0,scipy.stats.norm.pdf(pt1 ,mean1, std1)], color='black')

pt2 = mean1 - 3.5 * std1
plt.plot([pt2 ,pt2 ],[0.0,scipy.stats.norm.pdf(pt2 ,mean1, std1)], color='black')

ptx = np.linspace(pt1, pt2, 10)
pty = scipy.stats.norm.pdf(ptx,mean1,std1)

plt.fill_between(ptx, pty, color='yellow', alpha=1.0)

#----------------------------------------------------------------------------------------#

plt.grid()

plt.xlim(x_min,x_max1)
plt.ylim(0,0.25)

plt.title('In statistical hypothesis testing, a type I error is the rejection of a true null hypothesis, while a type II error is the non-rejection of a false null hypothesis',fontsize=10)

plt.xlabel('x')
plt.ylabel('Normal Distribution')

plt.savefig("normal_distribution.png")
plt.show()