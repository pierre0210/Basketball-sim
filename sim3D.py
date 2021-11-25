import basketball
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit, minimize
from mpl_toolkits.mplot3d import Axes3D

def altRange(start, end, step):
    return np.arange(start/step, end/step)*step

def func(x, a, b, c):
    return a*x**2+b*x+c

#Question 3 (3d)
fig = plt.figure()
ax = fig.gca(projection='3d')

ball3 = basketball.ball(mass=0.62, cw=0.5, airDensity=1.14)
angleList = np.linspace(10, 80, 20)
distanceList = np.linspace(6, 16, 20)
vList = np.array([])
lowerV = []
resultV = []

testAngle = [35, 45, 55]
for d in distanceList:
    for a in testAngle:
        print(str(d)+" "+str(a))
        for v in altRange(7, 17, 0.05):
            result = ball3.shoot(v, a, d)
            if result[2]:
                resultV.append(v)
        lowerV.append(resultV[0])
        resultV = []
    lowerpopt, lowerpcov = curve_fit(func, testAngle, lowerV)
    vList = np.append(vList, func(angleList, *lowerpopt))
    #print(vList)
    lowerV = []
    
angleList, distanceList = np.meshgrid(angleList, distanceList)
vList = np.reshape(vList, (20, 20))
ax.plot_surface(angleList, distanceList, vList, cmap='winter')
#ax.scatter(distanceList, angleList, vList)

ax.set_title("Question 3 (3D)")
ax.set_xlabel("angle")
ax.set_ylabel("distance")
ax.set_zlabel("velocity")
plt.legend()
plt.grid()
plt.show()