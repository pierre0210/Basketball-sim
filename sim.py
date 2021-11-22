import basketball
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit, minimize
from mpl_toolkits import mplot3d

def altRange(start, end, step):
    return np.arange(start/step, end/step)*step

def func(x, a, b, c):
    return a*x**2+b*x+c

curveX = np.linspace(7, 17, 1000)

#Question 1
print("Question 1")
ball1 = basketball.ball(mass=0.62)
vList = []
testDistance = [6.25, 7.6, 14]
testAngle = [35, 45, 55]
upperV = []
lowerV = []
angleX = np.linspace(30, 60, 3000)

for d in testDistance:
    for a in testAngle:
        for i in altRange(7, 17, 0.01):
            result = ball1.shoot(i, a, d)
            if result[2]:
                vList.append(i)
        lowerV.append(vList[0])
        upperV.append(vList[-1])
        vList = []
    lowerpopt, lowerpcov = curve_fit(func, testAngle, lowerV)
    print(str(d)+" m "+str(func(45, *lowerpopt)))
    #minimumObj = minimize(func, 45, (lowerpopt[0], lowerpopt[1], lowerpopt[2]))
    #print(str(d)+" m "+str(minimumObj.x)+" "+str(minimumObj.fun))
    plt.plot(angleX, func(angleX, *lowerpopt), label=str(d)+" m lower without air resistance")
    #upperpopt, upperpcov = curve_fit(func, testAngle, upperV)
    #plt.plot(angleX, func(angleX, *upperpopt), label=str(d)+" m upper")
    lowerV = []
    upperV = []
    

plt.xlabel("angle (degree)")
plt.ylabel("initial velocity (m/s)")
plt.legend()
plt.grid()
plt.show()

#Question 2
print("Question 2")
ball2 = basketball.ball(mass=0.62, cw=0.5, airDensity=1.14)
vList = []
testDistance = [6.25, 7.6, 14]
testAngle = [35, 45, 55]
upperV = []
lowerV = []
angleX = np.linspace(30, 60, 3000)

for d in testDistance:
    for a in testAngle:
        for i in altRange(7, 17, 0.01):
            result = ball2.shoot(i, a, d)
            if result[2]:
                vList.append(i)
        lowerV.append(vList[0])
        upperV.append(vList[-1])
        vList = []
    lowerpopt, lowerpcov = curve_fit(func, testAngle, lowerV)
    print(str(d)+" m "+str(func(45, *lowerpopt)))
    #minimumObj = minimize(func, 45, (lowerpopt[0], lowerpopt[1], lowerpopt[2]))
    #print(str(d)+" m "+str(minimumObj.x)+" "+str(minimumObj.fun))
    plt.plot(angleX, func(angleX, *lowerpopt), label=str(d)+" m lower with air resistance")
    #upperpopt, upperpcov = curve_fit(func, testAngle, upperV)
    #plt.plot(angleX, func(angleX, *upperpopt), label=str(d)+" m upper")
    lowerV = []
    upperV = []
    
plt.xlabel("angle (degree)")
plt.ylabel("initial velocity (m/s)")
plt.legend()
plt.grid()
plt.show()

#Question 3
#fig = plt.figure()
#ax = plt.axes(projection='3d')
print("Question 3")
angleX = np.linspace(30, 60, 3000)
ball3 = basketball.ball(mass=0.62, cw=0.5, airDensity=1.14)
vList = []
bestAngle = 0
lowestV = 20.0

upperV = []
lowerV = []

testDistance = [6.25, 7.6, 14]
#testDistance = np.linspace(6.25, 14, 80)
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
    #print(str(d)+" m "+str(func(45, *lowerpopt)))
    minimumObj = minimize(func, 45, (lowerpopt[0], lowerpopt[1], lowerpopt[2]))
    print(str(d)+" m "+str(minimumObj.x)+" "+str(minimumObj.fun))
    plt.scatter(minimumObj.x, minimumObj.fun)
    plt.plot(angleX, func(angleX, *lowerpopt), label=str(d)+" m lower")
    #upperpopt, upperpcov = curve_fit(func, testAngle, upperV)
    #plt.plot(angleX, func(angleX, *upperpopt), label=str(d)+" m upper")
    lowerV = []
    upperV = []

plt.xlabel("angle (degree)")
plt.ylabel("initial velocity (m/s)")
plt.legend()
plt.grid()
plt.show()


#Question 4
print("Question 4")
angleX = np.linspace(30, 60, 3000)
ball4 = basketball.ball(mass=0.62, cw=0.5, airDensity=1.14, omega=6)
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
            result = ball4.shoot(i, a, d)
            if result[2]:
                vList.append(i)
        lowerV.append(vList[0])
        upperV.append(vList[-1])
        vList = []
    lowerpopt, lowerpcov = curve_fit(func, testAngle, lowerV)
    print(str(d)+" m "+str(func(45, *lowerpopt)))
    minimumObj = minimize(func, 45, (lowerpopt[0], lowerpopt[1], lowerpopt[2]))
    print(str(d)+" m "+str(minimumObj.x)+" "+str(minimumObj.fun))
    plt.scatter(minimumObj.x, minimumObj.fun)
    plt.plot(angleX, func(angleX, *lowerpopt), label=str(d)+" m lower with spin")
    #upperpopt, upperpcov = curve_fit(func, testAngle, upperV)
    #plt.plot(angleX, func(angleX, *upperpopt), label=str(d)+" m upper with spin")
    lowerV = []
    upperV = []


plt.xlabel("angle (degree)")
plt.ylabel("initial velocity (m/s)")
plt.legend()
plt.grid()
plt.show()
