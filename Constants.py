import time
import random
import math
import sys

import pygame

pygame.init()
display = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
display_breedte, display_lengte = display.get_size()
pygame.mouse.set_pos(display_breedte,display_lengte)
gridx = 20
gridy = 20
gridb = display_breedte - gridx
gridl = display_lengte - gridy

wit = (255, 255, 255)
zwart = (0, 0, 0)
rood = (255, 0, 0)
groen = (0, 255, 0)
blauw = (25, 25, 255)
geel = (255, 255, 0)
oranje = (200, 60, 0)
grijs = (190, 200, 200)
cyanide = (0, 250, 250)
paars = (250, 0, 250)

creationspeed = 3
creationmass = [2] * 5 + [3] * 4 + [4] * 3 + [5] * 2 + [6]
creationcharge = 1

constant_coulomb = 10
active_distance = 50
amount = 180
amountflares = 3
friction = 0.015

protoncharge = 6
protonsize = 6
protonmass = 6

electroncharge = -2
electronsize = 2
electronmass = 2


attractorscale = 150
attractormass = 20
attractorelectronscale = 0.5

speedermass = 5
speederspeed = 5
speedersize = 2
speedercharge = 0


flaremass = 5
flarecharge = -2
flaresize = 3

chargedistribution = [0,0,1,1,1,-1,-1,-1,-1,-1]