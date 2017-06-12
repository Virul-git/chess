import numpy 
import pygame 
import itertools


#%%%%%%%%%%%%%%%%% FUNCTIONS REGARDING CHESS %%%%%%%%%%%%%%%%%%%#
def display_board(board):
	print board


def init():
	board = numpy.zeros((8,8))
	return board

def update_board(board,points):
	for a in points:
		board[a[0],a[1]]=1

def check(points):
	for a in points:
		for b in points:
			if a != b:
				if a[0] == b[0]:
					return False
				if a[1] == b[1]:
					return False
				if a[0]-b[0] == a[1]-b[1]:
					return False
				if a[0]-b[0] == b[1]-a[1]:
					return False
	return True			
def solve():
	taskRunning = True
	indexes = [0,1,2,3,4,5,6,7]
	pos_arr = [7,6,5,4,3,2,1,0]
	a = itertools.permutations(pos_arr)
	boards = []	
	comb = 0
	for j in a:
		board = init()
		points = zip(indexes,j)	
		if not check(points):
			continue
		update_board(board,points)
		display_board(board)
		boards.append(points)
		comb= comb+1
		#print "this a valid combination, no."+str(comb)
	return boards
#%%%%%%%%%%%%%%%%%%%% END OF CHESS FUNCTIONS %%%%%%%%%%%%%%%%%%%%#
display_width = 420
display_height = 420
	
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue =(0,0,255)

pygame.init()


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("BOX")


def drawBox(gameDisplay):
	gameDisplay.fill(black)
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

def add_pawn(gameDisplay,center):
	pygame.draw.circle(gameDisplay,red,center,20)
	

def gameloop():
	gamerunning = True
	pixAr = pygame.PixelArray(gameDisplay)
	boards = solve()
	while True:
		try:
			a = int(raw_input("select a combination among the 92:"))
		except:
			print "ERROR: Invalid input!!!!!!!!!. Enter a valid number(1-92)"
			print "(OR) enter 0 to exit"

		if (a<0 or a>92):
			continue
		if a==0:
			pygame.quit()
			quit()
			break
		drawBox(gameDisplay)
		print boards[a-1]
		for k in boards[a-1]:
			s = (k[0]*50+35,k[1]*50+35)
			add_pawn(gameDisplay,s)
			print s
		pygame.display.update()
		
		


if __name__ == "__main__":
	gameloop()
