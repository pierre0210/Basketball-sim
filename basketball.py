import numpy as np

class ball:
    def __init__(self, distance, mass, height=3.05, ballD=0.24, rimD=0.4572, angle=45, cw=0, density=0, g=9.8):
        self.dis = distance
        self.mass = mass
        self.height = height
        self.ballD = ballD
        self.rimD = rimD
        self.angle = angle
        self.cw = cw
        self.density = density
        self.g = g
        self.xpos = 0
        self.ypos = 2
        self.dt = 0.01

    def clear(self):
        self.xpos = 0
        self.ypos = 2
        #self.curTime = 0

    def shoot(self, v, av=0):
        self.clear()
        xlist = []
        ylist = []
        isInRange = False
        self.vx = v*np.cos(self.angle*np.pi/180.0)
        self.vy = v*np.sin(self.angle*np.pi/180.0)
        self.od = self.distance(self.xpos, self.ypos)
        while True:
            self.xpos += self.vx*self.dt
            self.ypos += self.vy*self.dt

            self.vy -= self.g*self.dt
            xlist.append(self.xpos)
            ylist.append(self.ypos)
            if self.distance(self.xpos, self.ypos) > self.od:
                self.od = self.distance(self.xpos, self.ypos)
                break
            elif self.distance(self.xpos, self.ypos) <= self.rimD-self.ballD:
                isInRange = True
                break
            else:
                self.od = self.distance(self.xpos, self.ypos)
        
        return [xlist, ylist, isInRange]

    def distance(self, bx, by):
        return ((self.dis-bx)**2+(self.height-by)**2)**0.5

    def error(self, bx, by):
        slope = -np.cos(self.angle*np.pi/180.0)/np.sin(self.angle*np.pi/180.0)
        state = slope*(bx-self.dis)-self.height
        if(by >= state):
            return self.distance(bx, by)
        else:
            return -self.distance(bx, by)
