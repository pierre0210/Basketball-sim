import numpy as np

class ball:
    def __init__(self, mass, height=3.05, ballD=0.24, rimD=0.4572, cw=0, airDensity=0, g=9.8, omega=0.0):
        self.mass = mass
        self.height = height
        self.ballD = ballD
        self.rimD = rimD
        self.cw = cw
        self.density = airDensity
        self.g = g
        self.omega = omega
        self.xpos = 0
        self.ypos = 2
        self.dt = 0.005

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
            df = self.dragForce(self.vx, self.vy)
            lf = self.liftForce(self.vx, self.vy)
            self.xpos += self.vx*self.dt
            self.ypos += self.vy*self.dt
            #print(df)
            self.vx += -df[0]*self.dt/self.mass-lf[0]*self.dt/self.mass
            self.vy += -self.g*self.dt-df[1]*self.dt/self.mass-lf[1]*self.dt/self.mass          
            #print(str(self.vx)+" "+str(self.vy))
            xlist.append(self.xpos)
            ylist.append(self.ypos)
            if self.distance(self.xpos, self.ypos) > self.od:
                #self.od = self.distance(self.xpos, self.ypos)
                break
            #elif self.distance(self.xpos, self.ypos) <= self.rimD/2-self.ballD/2 and self.height > self.ypos:
                #self.od = self.distance(self.xpos, self.ypos)
                #break
            elif self.distance(self.xpos, self.ypos) <= self.rimD/2-self.ballD/2:
                isInRange = True
                break
            else:
                self.od = self.distance(self.xpos, self.ypos)
        
        return [xlist, ylist, isInRange, self.od]

    def getRimRange(self):
        return self.rimD/2-self.ballD/2

    def distance(self, bx, by):
        return ((self.dis-bx)**2+(self.height-by)**2)**0.5

    def dragForce(self, vx, vy):
        #curAngle = np.arctan(vy/vx)
        dragForce = 0.5*self.cw*self.density*((self.ballD/2)**2)*np.pi*(vx**2+vy**2)
        return [dragForce*vx/((vx**2+vy**2)**0.5), dragForce*vy/((vx**2+vy**2)**0.5)]

    def liftForce(self, vx, vy):
        if self.omega == 0:
            return [0, 0]
        cl = 1/(2+(vx**2+vy**2)**0.5/((self.ballD/2)*self.omega))
        liftForce = 0.5*cl*((self.ballD/2)**2)*np.pi*(vx**2+vy**2)
        return [liftForce*vy/((vx**2+vy**2)**0.5), -liftForce*vx/((vx**2+vy**2)**0.5)]

    def error(self, bx, by):
        slope = -np.cos(self.angle*np.pi/180.0)/np.sin(self.angle*np.pi/180.0)
        state = slope*(bx-self.dis)-self.height
        if(by >= state):
            return self.distance(bx, by)
        else:
            return -self.distance(bx, by)
