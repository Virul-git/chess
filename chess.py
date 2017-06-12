import numpy 
import itertools

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
	comb = 0
	for j in a:
		board = init()
		points = zip(indexes,j)	
		if not check(points):
			continue
		update_board(board,points)
		display_board(board)
		comb= comb+1
		print "this a valid combination, no."+str(comb)


if __name__ == "__main__":
	solve()
