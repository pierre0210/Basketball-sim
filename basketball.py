import numpy as np

class ball:
    def __init__(self, mass, height=3.05, ballD=0.24, rimD=0.4572, cw=0, airDensity=0, g=9.8):
        self.mass = mass
        self.height = height
        self.ballD = ballD
        self.rimD = rimD
        self.cw = cw
        self.density = airDensity
        self.g = g
        self.xpos = 0
        self.ypos = 2
        self.dt = 0.01

    def clear(self):
        self.xpos = 0
        self.ypos = 2
        #self.curTime = 0

    def shoot(self, v, angle, distance):
        self.clear()
        self.angle = angle
        self.dis = distance
        xlist = []
        ylist = []
        isInRange = False
        self.vx = v*np.cos(self.angle*np.pi/180.0)
        self.vy = v*np.sin(self.angle*np.pi/180.0)
        self.od = self.distance(self.xpos, self.ypos)
        while True:
            df = self.force(self.vx, self.vy)
            self.xpos += self.vx*self.dt
            self.ypos += self.vy*self.dt

            self.vx -= (df[0]/self.mass)*self.dt
            self.vy -= (self.g+(df[1]/self.mass))*self.dt
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

    def force(self, vx, vy):
        dragForce = 0.5*self.cw*self.density*((self.ballD/2)**2)*np.pi*(vx**2+vy**2)
        return [dragForce*np.cos(self.angle*np.pi/180.0), dragForce*np.sin(self.angle*np.pi/180.0)]

    def error(self, bx, by):
        slope = -np.cos(self.angle*np.pi/180.0)/np.sin(self.angle*np.pi/180.0)
        state = slope*(bx-self.dis)-self.height
        if(by >= state):
            return self.distance(bx, by)
        else:
            return -self.distance(bx, by)
