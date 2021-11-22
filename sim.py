import basketball
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit, minimize

def altRange(start, end, step):
    return np.arange(start/step, end/step)*step

def func(v, a, b, c):
    return a*v**2+b*v+c

curveX = np.linspace(7, 17, 1000)
'''
#Question 1
print("Question 1")
ball1 = basketball.ball(mass=0.62)
vList = []
testDistance = [6.25, 7.6, 14]

for d in testDistance:
    distanceToRim = []
    for i in altRange(7.0, 17.0, 0.01):
        i = round(i, 2)
        result = ball1.shoot(i, 45, d)
        distanceToRim.append(result[3])
        if result[2]:
            vList.append(i)
            #plt.scatter(result[0], result[1])
    vList = [vList[0], vList[-1]]
    print(vList)
    vList = []
    plt.plot(curveX, distanceToRim, label=str(d)+" m without air resistance")

#plt.grid()
#plt.show()


#Question 2
print("Question 2")
ball2 = basketball.ball(mass=0.62, cw=0.5, airDensity=1.14)
testSpeed = [5, 11, 17]
testDistance = [6.25, 7.6, 14]

vList = []

for d in testDistance:
    distanceToRim = []
    for i in altRange(7, 17, 0.01):
        result = ball2.shoot(i, 45, d)
        distanceToRim.append(result[3])
        if result[2]:
            vList.append(i)
    vList = [vList[0], vList[-1]]
    print(vList)
    vList = []
    #popt, pcov = curve_fit(func, curveX, distanceToRim)
    #plt.plot(curveX, func(curveX, *popt))
    plt.plot(curveX, distanceToRim, label=str(d)+" m with air resistance")
    #solve = fsolve(func, [0, ball2.getRimRange()], args=(popt[0], popt[1], popt[2]))
    #print(solve)

#plt.scatter(testSpeed, distanceToRim)
plt.legend()
plt.grid()
plt.show()
'''

#Question 3
angleX = np.linspace(30, 60, 3000)
ball3 = basketball.ball(mass=0.62, cw=0.5, airDensity=1.14)
vList = []
bestAngle = 0
lowestV = 20.0

upperV = []
lowerV = []

testDistance = [6.25, 7.6, 14]
testAngle = [45, 50, 55]

for d in testDistance:
    for a in testAngle:
        for i in altRange(7, 17, 0.01):
            result = ball3.shoot(i, a, d)
            if result[2]:
                vList.append(i)
        lowerV.append(vList[0])
        upperV.append(vList[-1])
        vList = []
    lowerpopt, lowerpcov = curve_fit(func, testAngle, lowerV)
    minimumObj = minimize(func, 45, (lowerpopt[0], lowerpopt[1], lowerpopt[2]))
    print(str(d)+" m "+str(minimumObj.x)+" "+str(minimumObj.fun))
    plt.plot(angleX, func(angleX, *lowerpopt), label=str(d)+" m lower")
    upperpopt, upperpcov = curve_fit(func, testAngle, upperV)
    plt.plot(angleX, func(angleX, *upperpopt), label=str(d)+" m upper")
    lowerV = []
    upperV = []

plt.legend()
plt.grid()
plt.show()
