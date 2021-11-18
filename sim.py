import basketball
import matplotlib.pyplot as plt
import numpy as np

def altRange(start, end, step):
    return np.arange(start/step, end/step)*step
'''
#Question 1

ball1 = basketball.ball(mass=0.62)
vList = []

for i in altRange(5.0, 20.0, 0.01):
    i = round(i, 2)
    result = ball1.shoot(i, 45, 6.25)
    if result[2]:
        vList.append(i)
        #plt.scatter(result[0], result[1])

vList = [vList[0], vList[-1]]
print(vList)
#plt.grid()
#plt.show()
'''
'''
#Question 2

ball2 = basketball.ball(mass=0.62, cw=0.5, airDensity=1.14)
vList = []

for i in altRange(10.0, 20.0, 0.01):
    i = round(i, 2)
    #print(i)
    result = ball2.shoot(i, 45, 14)
    if result[2]:
        vList.append(i)
        #plt.scatter(result[0], result[1])

resultList = [vList[0], vList[-1]]
print(resultList)
#plt.grid()
#plt.show()
'''

#Question 3

ball3 = basketball.ball(mass=0.62, cw=0.0, airDensity=1.14)
vList = []
bestAngle = 0
lowestV = 20.0

angle = []
v = []

for i in np.arange(45.0, 55.0, 1.0):
    #i = round(i, 1)
    for j in altRange(5.0, 15.0, 0.001):
        #j = round(j, 2)
        result = ball3.shoot(j, i, 6.25)
        if result[2]:
            print(i, j)
            angle.append(i)
            v.append(j)
            plt.scatter(result[0], result[1])
            if lowestV >= j:
                bestAngle = i
                lowestV = j
            break
#plt.scatter(angle, v)
plt.grid()
plt.show()

print("best angle: "+str(bestAngle))
print("lowest velocity: "+str(lowestV))
