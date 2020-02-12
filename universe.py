import pygame
from sys import exit
from random import *
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

startcolors ={
	0 : (255,255,255),
	1 : (255,0,0),
	2 : (0,0,255),
	3 : (0,255,0),
	4 : (randrange(0,255),randrange(0,255),randrange(0,255))}

lehmer = 0
galaxy_offset = [20000,0]
def Lehmer():
	global lehmer
	lehmer += 0xe120fc15
	tmp = lehmer*0x4a39b70d
	m1 = (tmp>>32) ^ tmp
	tmp = m1*0x12fad5c9
	m2 = (tmp>>32) ^ tmp
	return m2
width = 1000
height = 1000
WHITE = (255,255,255)
BLACK = (0,0,0)
resolution = 10
SPEED = 100
row = height//resolution
col = width//resolution
pygame.init()
window = pygame.display.set_mode((width,height))
fps = pygame.time.Clock()
bro ={}
ellapsedtime = 0
w,z=0,0
while(1):
	w,z = 0,0
	fps.tick(12)
	ellapsedtime = pygame.time.get_ticks() - ellapsedtime
	window.fill(pygame.Color(0,0,0))
	for event in pygame.event.get():
		if event.type==pygame.KEYDOWN:
			if event.key == pygame.K_q:
				pygame.quit()
				exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			w,z = event.pos
			w//=resolution
			z//=resolution
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_a]:
		galaxy_offset[0]-=SPEED
	if pressed[pygame.K_d]:
		galaxy_offset[0]+=SPEED
	if pressed[pygame.K_w]:
		galaxy_offset[1]-=SPEED
	if pressed[pygame.K_s]:
		galaxy_offset[1]+=SPEED
	start = time.time()
	for i in range(row):
		for j in range(col):
			x,y = (i*resolution),(j*resolution)
			x_coord,y_coord = x+galaxy_offset[0],y+galaxy_offset[1]
			w_coord,z_coord = w*resolution,z*resolution
			seed = (y_coord) << 16 | (x_coord)
			lehmer = seed
			color = Lehmer()%5
			radius = Lehmer()%7 + 1
			isS = Lehmer()%400 + 1 == 1
			if(isS):
				pygame.draw.circle(window, startcolors[color], (x+5,y+5), radius)
				if(w_coord == x and z_coord==y):
					pygame.draw.circle(window, (255,0,0), ((w*resolution)+5,(z*resolution)+5), radius)
					if((w_coord+galaxy_offset[0],z_coord+galaxy_offset[1]) not in bro.keys()):
						bro[(w_coord+galaxy_offset[0],z_coord+galaxy_offset[1])] = "KNOW STAR"
					#pygame.draw.circle(window, (255,0,0), ((w*resolution)+5,(z*resolution)+5), 10)
					else:
						print(bro[(w_coord+galaxy_offset[0],z_coord+galaxy_offset[1])])
						
	end = time.time()

	#print(bcolors.OKBLUE + "Done" + bcolors.ENDC + "  " + bcolors.WARNING + str(end-start) + bcolors.ENDC)
	pygame.display.flip()
