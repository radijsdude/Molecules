
from Constants import *


def distance(quark1,quark2):
    xa,ya = quark1.get_position()
    xb,yb = quark2.get_position()
    return ((xa - xb) ** 2 + (ya - yb) ** 2) ** (1/2)

def speeddifferende(quark1,quark2):
    return ((quark1.vx - quark2.vx) ** 2 + (quark1.y - quark2.y)**2)**(1/2)

def centerofmass(quark1,quark2):
    x = 0
    y = 0
    m = quark1.m + quark2.m
    x += quark1.m * quark1.x + quark2.m * quark2.x
    y += quark1.m * quark1.y + quark2.m * quark2.y
    x /= m
    y /= m
    return x,y,m



def quark_collide(quark1,quark2):
    r = quark1.size + quark2.size
    d = distance(quark1,quark2)
    collide = False
    if d <= r:
        collide = True
    return collide
def quark_collission(quark1,quark2):
    m1 = quark1.m
    m2 = quark2.m
    d = distance(quark1,quark2)
    if d == 0:
        d = 0.01

    cosY = (quark2.x - quark1.x) / d
    sinY = (quark2.y - quark1.y) / d
    v1x = quark1.vx
    v1y = quark1.vy
    v2x = quark2.vx
    v2y = quark2.vy
    v10 = ((v1x * cosY + v1y * sinY) * (m1 - m2) + 2 * m2 * (v2x * cosY + v2y * sinY)) * cosY / (m1 + m2) - (
                                                                                                                     v1y * cosY - v1x * sinY) * sinY
    v11 = ((v1x * cosY + v1y * sinY) * (m1 - m2) + 2 * m2 * (v2x * cosY + v2y * sinY)) * sinY / (m1 + m2) + (
                                                                                                                     v1y * cosY - v1x * sinY) * cosY
    v20 = ((v2x * cosY + v2y * sinY) * (m2 - m1) + 2 * m1 * (v1x * cosY + v1y * sinY)) * cosY / (m1 + m2) - (
                                                                                                                     v2y * cosY - v2x * sinY) * sinY
    v21 = ((v2x * cosY + v2y * sinY) * (m2 - m1) + 2 * m1 * (v1x * cosY + v1y * sinY)) * sinY / (m1 + m2) + (
                                                                                                                     v2y * cosY - v2x * sinY) * cosY
    quark1.vx = v10
    quark1.vy = v11
    quark2.vx = v20
    quark2.vy = v21
    dc = 1
    if quark1.x > quark2.x:
        quark1.x += dc
        quark2.x -= dc
    else:
        quark1.x -= dc
        quark2.x += dc

    if quark1.y > quark2.y:
        quark1.y += dc
        quark2.y -= dc
    else:
        quark1.y -= dc
        quark2.y += dc


def quark_force_coulomb(quark1,quark2):
    x1,y1 = quark1.get_position()
    q1 = quark1.q
    m1 = quark1.m
    x2,y2 = quark2.get_position()
    q2 = quark2.q
    dx = x1 - x2
    dy = y1 - y2
    r = distance(quark1,quark2)
    if r < quark1.size+quark2.size:
        r = quark1.size+quark2.size
    a = constant_coulomb * q1 * q2 /(m1 * r ** 3)
    ax = a * dx
    ay = a * dy
    quark1.ax += ax
    quark1.ay += ay

class Quark:
    def __init__(self,size=2,x=0,y=0,vx=0,vy=0,ax=0,ay=0,m=1,q=1,color=groen,tag='quark',parent=None):
        self.name = str(random.randrange(1000)) + str(random.randrange(1000))
        self.size = size
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay
        self.m = m
        self.q = q
        self.color = color
        self.tag = tag
        if q < 0:
            self.color = rood
        if q > 0:
            self.color = blauw
        if tag == 'speeder':
            self.color = geel
        if self.tag == 'flare':
            self.color = wit
        if self.tag == 'attractor':
            self.color = oranje

        self.parent = parent
        self.timer = 5
    def friction(self):
        if self.q < 0:
            self.vx -= friction * self.vx
            self.vy -= friction * self.vy
    def get_position(self):
        return self.x,self.y
    def reset_acceleration(self):
        self.ax = 0
        self.ay = 0
    def accelerate(self):
        self.friction()
        self.vx += self.ax
        self.vy += self.ay
        if self.tag == 'speeder' or self.tag == 'flare':
            angle = math.atan2(self.vy,self.vx)
            self.vx = speederspeed * math.cos(angle)
            self.vy = speederspeed * math.sin(angle)
        if self.tag == 'attractor':
            self.vx -= (self.x - display_breedte/2)/attractorscale
            self.vy -= (self.y - display_lengte/2)/attractorscale

    def move(self):
        if self.timer > 0:
            self.timer -= 1
        self.x += self.vx
        self.y += self.vy
        if self.x < gridx:
            self.x = gridx
            self.vx = -self.vx
        if self.x > gridb:
            self.x = gridb
            self.vx = -self.vx
        if self.y < gridy:
            self.y = gridy
            self.vy = -self.vy
        if self.y > gridl:
            self.y = gridl
            self.vy = -self.vy

    def blits(self):
        return self.color,[int(self.x),int(self.y)],self.size



