import numpy 
import pygame 


display_width = 1024
display_height = 768
	
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
	pygame.draw.line(gameDisplay,blue,(100,100),(100,900))
	pygame.draw.line(gameDisplay,blue,(100,900),(900,900))
	pygame.draw.line(gameDisplay,blue,(900,900),(900,100))
	pygame.draw.line(gameDisplay,blue,(900,100),(100,100))

def hero(xy):
	

def gameloop():
	gamerunning = True
	pixAr = pygame.PixelArray(gameDisplay)
	while gamerunning:
		drawBox(gameDisplay)
		input_from_user()
		pygame.display.update()


if __name__ == "__main__":
	gameloop()
