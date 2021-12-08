import basketball
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit, minimize

def altRange(start, end, step):
    return np.arange(start/step, end/step)*step

def func(x, a, b, c):
    return a*x**2+b*x+c

ball = basketball.ball(0.62)

vList = []
testDistance = [6.25, 7.6, 14]
testAngle = [35, 45, 55]
upperV = []
lowerV = []
angleX = np.linspace(30, 60, 3000)

for d in testDistance:
    for a in testAngle:
        for i in altRange(7, 17, 0.01):
            result = ball.shoot(i, a, d)
            if result[2]:
                vList.append(i)
        lowerV.append(vList[0])
        upperV.append(vList[-1])
        vList = []
    lowerpopt, lowerpcov = curve_fit(func, testAngle, lowerV)
    v = func(45, *lowerpopt)
    curResult = ball.shoot(v, 45, d)
    ypos = curResult[1]
    vx = curResult[4]
    vy = curResult[5]
    timestampList = curResult[6]
    peList = []
    keList = []
    energyList = []

    for y, vvx, vvy in zip(ypos, vx, vy):
        pe = y*0.62*9.8
        ke = 0.5*0.62*(vvx**2+vvy**2)
        peList.append(pe)
        keList.append(ke)
        energyList.append(pe+ke)

    plt.plot(timestampList, peList, label="PE")
    plt.plot(timestampList, keList, label="KE")
    plt.plot(timestampList, energyList, label="E")
    plt.grid()
    plt.title(str(d)+" m")
    plt.legend()
    plt.show()
    #minimumObj = minimize(func, 45, (lowerpopt[0], lowerpopt[1], lowerpopt[2]))
    #print(str(d)+" m "+str(minimumObj.x)+" "+str(minimumObj.fun))
    #plt.plot(angleX, func(angleX, *lowerpopt), label=str(d)+" m lower without air resistance")
    #upperpopt, upperpcov = curve_fit(func, testAngle, upperV)
    #plt.plot(angleX, func(angleX, *upperpopt), label=str(d)+" m upper")
    lowerV = []
    upperV = []