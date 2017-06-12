import numpy 
import pygame 


display_width = 420
display_height = 420
	
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue =(0,0,255)

pygame.init()


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("BOX")

def input_from_user():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

def drawBox(gameDisplay):
	################## BASIC BOX	####################
	pygame.draw.line(gameDisplay,blue,(10,10),(10,410))
	pygame.draw.line(gameDisplay,blue,(10,410),(410,410))
	pygame.draw.line(gameDisplay,blue,(410,410),(410,10))
	pygame.draw.line(gameDisplay,blue,(410,10),(10,10))
	#################	INTERNAL LINES	#################
	pygame.draw.line(gameDisplay,blue,(60,10),(60,410))
	pygame.draw.line(gameDisplay,blue,(110,10),(110,410))
	pygame.draw.line(gameDisplay,blue,(160,10),(160,410))
	pygame.draw.line(gameDisplay,blue,(210,10),(210,410))
	pygame.draw.line(gameDisplay,blue,(260,10),(260,410))
	pygame.draw.line(gameDisplay,blue,(310,10),(310,410))
	pygame.draw.line(gameDisplay,blue,(360,10),(360,410))
	################## HORIZONTAL ####################
	pygame.draw.line(gameDisplay,blue,(410,60),(10,60))
	pygame.draw.line(gameDisplay,blue,(410,110),(10,110))
	pygame.draw.line(gameDisplay,blue,(410,160),(10,160))
	pygame.draw.line(gameDisplay,blue,(410,210),(10,210))
	pygame.draw.line(gameDisplay,blue,(410,260),(10,260))
	pygame.draw.line(gameDisplay,blue,(410,310),(10,310))
	pygame.draw.line(gameDisplay,blue,(410,360),(10,360))
	################# VERTICAL	######################

def hero(xy,gameDisplay):
	pygame.draw.rect(gameDisplay,blue,xy,20,20)	

def gameloop():
	gamerunning = True
	pixAr = pygame.PixelArray(gameDisplay)
	xy = (200,200)
	while gamerunning:
		drawBox(gameDisplay)
		input_from_user()
		pygame.display.update()


if __name__ == "__main__":
	gameloop()
