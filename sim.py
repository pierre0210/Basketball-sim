import basketball
import matplotlib.pyplot as plt
import numpy as np

ball = basketball.ball(14.0, 10.0)

vList = []

for i in np.arange(0.0, 20.0, 0.01):
    result = ball.shoot(i)
    if result[2]:
        vList.append(i)
        plt.scatter(result[0], result[1])

plt.grid()
plt.show()