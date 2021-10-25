import basketball
import matplotlib.pyplot as plt
import numpy as np

def altRange(start, end, step):
    return np.arange(start/step, end/step)*step
'''
#Question 1

ball1 = basketball.ball(mass=0.62)
vList = []

for i in altRange(10.0, 20.0, 0.01):
    i = round(i, 2)
    result = ball1.shoot(i, 45, 14.0)
    if result[2]:
        vList.append(i)
        #plt.scatter(result[0], result[1])

vList = [vList[0], vList[-1]]
print(vList)
#plt.grid()
#plt.show()
'''
#Question 2

ball2 = basketball.ball(mass=0.62, cw=0.5, airDensity=1.14)
vList = []

for i in altRange(10.0, 20.0, 0.01):
    i = round(i, 2)
    #print(i)
    result = ball2.shoot(i, 45, 14.0)
    if result[2]:
        vList.append(i)
        #plt.scatter(result[0], result[1])

vList = [vList[0], vList[-1]]
print(vList)
#plt.grid()
#plt.show()
'''
#Question 3

ball3 = basketball.ball(mass=0.62, cw=0.5, airDensity=1.14)
vList = []
bestAngle = 0
lowestV = 20.0

for i in range(20, 50):
    for j in altRange(10.0, 20.0, 0.01):
        j = round(j, 2)
        #print(str(i)+" "+str(j))
        result = ball3.shoot(j, i, 7.6)
        if result[2]:
            if lowestV > j:
                bestAngle = i
                lowestV = j
            break

print("best angle: "+str(bestAngle))
print("lowest velocity: "+str(lowestV))
'''