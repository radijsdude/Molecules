import time
import random
import math

import pygame

pygame.init()
display = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
display_breedte, display_lengte = display.get_size()
gridx = 20
gridy = 20
gridb = display_breedte - gridx
gridl = display_lengte - gridy

wit = (255, 255, 255)
zwart = (0, 0, 0)
rood = (255, 100, 100)
groen = (100, 255, 100)
blauw = (100, 100, 255)
geel = (255, 255, 0)
oranje = (255, 60, 0)
grijs = (190, 200, 200)
cyanide = (0, 250, 250)
paars = (250, 0, 250)

creationspeed = 3
creationmass = [2] * 5 + [3] * 4 + [4] * 3 + [5] * 2 + [6]
creationcharge = 1

constant_coulomb = 6
active_distance = 50
amount = 200
amountflares = 5
friction = 0.02

protonsize = 6
electronsize = 2

chargeproton = 8
chargeelectron = -2

speederspeed = 5

attractorscale = 400