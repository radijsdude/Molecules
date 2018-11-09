
from Quark import *

def explode(quark1,quark2):
    cx,cy,cm = centerofmass(quark1,quark2)
    l = []
    for i in range(int(cm/2)):
        vx = random.randrange(-creationspeed,creationspeed +1)
        vy = random.randrange(-creationspeed,creationspeed +1)
        newquark = Quark(size=2,m=2,x=cx+2*vx,y=cy+2*vy,q=0,vx=vx,vy=vy,tag='quark')
        l.append(newquark)
    return l

def fission(quark1):
    uncertainty = 4
    cx, cy = quark1.get_position()
    l = []
    for i in range(quark1.m):
        ux = random.randrange(-uncertainty, uncertainty + 1)
        uy = random.randrange(-uncertainty, uncertainty + 1)
        vx = random.randrange(-creationspeed, creationspeed + 1)
        vy = random.randrange(-creationspeed, creationspeed + 1)
        newquark = Quark(size=1, m=1, x=cx + ux, y=cy + uy, q=0, vx=vx, vy=vy, tag='quark')
        l.append(newquark)
    return l

def merge(quark1,quark2):
    uncertainty = 4
    cx,cy,cm = centerofmass(quark1,quark2)
    vx = quark1.m * quark1.vx + quark2.m * quark2.vx
    vy = quark1.m * quark1.vy + quark2.m * quark2.vy
    vx /= cm
    vy /= cm
    l = []
    if cm < protonsize:
        newquark = Quark(m=cm,x=cx,y=cy,vx=vx,vy=vy,q=0,size=cm,tag='quark')
    elif cm == protonsize:
        newquark = Quark(m=cm,x=cx,y=cy,vx=vx,vy=vy,q=cm,size=cm,tag='proton')
    else:
        newquark = Quark(m=cm,x=cx,y=cy,vx=vx,vy=vy,q=cm,size=protonsize,tag='proton')
        for i in range(int((cm-protonsize)/2)):
            ux = random.randrange(-uncertainty,uncertainty +1)
            uy = random.randrange(-uncertainty,uncertainty +1)
            vx = random.randrange(-creationspeed,creationspeed +1)
            vy = random.randrange(-creationspeed,creationspeed +1)
            l.append(Quark(m=2,x=cx+ux,y=cy+uy,vx=vx,vy=vy,q=0,tag='quark',size=2))

    l.append(newquark)
    return l

def newspeeder(quark1,quark2):
    x,y,m = centerofmass(quark1,quark2)
    rvx = quark1.vx - quark2.vx
    rvy = quark1.vy - quark2.vy
    angle = math.atan2(rvy,rvx)
    angle += random.choice([math.pi/2,-math.pi/2])
    vx = speederspeed * math.cos(angle)
    vy = speederspeed * math.sin(angle)
    name = ''.join(sorted([quark1.name,quark2.name]))
    return Quark(x=x+vx,y=y+vy,m=5,vx=vx,vy=vy,size=2,tag='speeder',parent=name,q=0)


def place_newquark(handler):
    vx = random.randrange(-creationspeed, creationspeed +1)
    vy = random.randrange(-creationspeed, creationspeed +1)
    m = random.choice(creationmass)
    q = random.choice([0,1,-1,-1,-1])
    if q < 0:
        m = 2
        tag = 'electron'
        q = chargeelectron
        size = 2
    elif q > 0:
        m = protonsize
        size = protonsize
        q = chargeproton
        tag='proton'
    else:
        tag='quark'
        size = m

    newquark = Quark(vx=vx,vy=vy,q=q,m=m,size=size,tag=tag)
    safetoplace(handler,newquark)
def safetoplace(handler,newquark):
    t = True
    spacing = 5

    x = random.randrange(gridx + spacing, gridb - spacing)
    y = random.randrange(gridy + spacing, gridl - spacing)
    newquark.x = x
    newquark.y = y
    for quark in handler.quarks:
        if quark_collide(newquark, quark):
            t = False
            break
    while not t:
        t = True
        x = random.randrange(gridx + spacing, gridb - spacing)
        y = random.randrange(gridy + spacing, gridl - spacing)
        newquark.x = x
        newquark.y = y
        for quark in handler.quarks:
            if quark_collide(newquark, quark):
                t = False
                break
    handler.quarks.append(newquark)


class Handler:
    def __init__(self,amount):
        self.quarks = [Quark(m=30,size=20,q=-50,tag='attractor',x=display_breedte/2,y=display_lengte/2)]
        self.quarks += [Quark(m=30,size=20,q=-50,tag='attractor',x=display_breedte/2+100,y=display_lengte/2+100)]
        self.count = 0
        for i in range(amount):
            place_newquark(self)
        for i in range(amountflares):
            safetoplace(self,Quark(m=5,size=3,tag='flare',q=0))

    def doe(self):
        newbies = []
        deletes = []
        names = []
        for i,quark1 in enumerate(self.quarks):
            if i not in deletes:
                if quark1.name in names:
                    print('double')
                    quark1.name += str(random.randrange(1000))
                names.append(quark1.name)
                for j,quark2 in enumerate(self.quarks):
                    if j not in deletes:
                        d = distance(quark1,quark2)
                        t1 = quark1.tag == 'attractor' and quark2.tag == 'proton'
                        t2 = quark2.tag == 'attractor' and quark1.tag == 'proton'
                        t = t1 or t2
                        if d < active_distance or t:
                            if quark1.name != quark2.name:
                                if quark1.q != 0 and quark2.q !=0:
                                    if quark1.tag == 'attractor' and quark2.tag == 'electron':
                                        pass
                                    elif quark2.tag == 'attractor' and quark1.tag == 'electron':
                                        pass
                                    else:
                                        quark_force_coulomb(quark1,quark2)

                                if quark_collide(quark1,quark2):

                                    quark_collission(quark1, quark2)

                                    if quark1.tag == 'quark' and quark2.tag == 'quark':
                                        l = merge(quark1,quark2)
                                        if len(l) > 1:
                                            for _ in range(int((len(l) + 1)/2)):
                                                l.append(newspeeder(quark1,quark2))
                                        newbies += l
                                        if i not in deletes:
                                            deletes.append(i)
                                        if j not in deletes:
                                            deletes.append(j)
                                        break

                                    elif quark1.tag == 'proton' and quark2.tag == 'proton':
                                        l = explode(quark1,quark2)
                                        for _ in range(int((len(l)) / 2)):
                                            l.append(newspeeder(quark1, quark2))
                                        newbies += l
                                        if i not in deletes:
                                            deletes.append(i)
                                        if j not in deletes:
                                            deletes.append(j)
                                        break
                                    elif quark1.tag == 'electron' and quark2.tag == 'electron':
                                        newbies.append(newspeeder(quark1,quark2))
                                    elif quark1.tag == 'speeder' and quark2.tag == 'speeder':
                                        if quark1.parent != quark2.parent:
                                            if quark1.timer == 0 and quark2.timer == 0:
                                                if speeddifferende(quark1,quark2) > speederspeed:
                                                    newbies.append(newspeeder(quark1,quark2))
                                        else:
                                            if i not in deletes:
                                                deletes.append(i)
                                            if j not in deletes:
                                                deletes.append(j)

                                    else:
                                        if quark1.tag == 'speeder':
                                            if quark2.tag != 'electron':
                                                if quark2.tag != 'quark':
                                                    if quark2.tag != 'flare':
                                                        if i not in deletes:
                                                            deletes.append(i)

                                        if quark2.tag == 'speeder':
                                            if quark1.tag != 'electron':
                                                if quark1.tag != 'quark':
                                                    if quark1.tag != 'flare':
                                                        if j not in deletes:
                                                            deletes.append(j)



                quark1.accelerate()
                quark1.move()
                quark1.reset_acceleration()
        for i in sorted(deletes)[::-1]:
            self.quarks.pop(i)
        for i in newbies:
            self.quarks.append(i)
    def blits(self):
        l = []
        for quark in self.quarks:
            l.append(quark.blits())
        return l


