import MovementUtils
import GenericUtils

def InitSnake():
	clear()
	change_hat(Hats.Dinosaur_Hat)
	next_x, next_y = measure()
	return next_x, next_y

def AfterMoveList(snakeList,new_x,new_y):
	snakeListAfter = []
	for i in range(len(snakeList)):
		snakeListAfter.append(snakeList[i])
	return snakeListAfter
	
def ChooseStart(snakeList):
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			if not(GenericUtils.Exists(snakeList,(x,y),MovementUtils.CompareCoordinates)):
				return x,y				

def VerifyMove(x,y,snakeListAfter):
	return True
	
def VerifyMoveTooSlow(x,y,snakeListAfter):
	x,y = ChooseStart(snakeListAfter)
	world = []
	onlyHas0 = True
	total_zeros = 0
	for i in range(get_world_size()):
		line = []
		for j in range(get_world_size()):
			if not(GenericUtils.Exists(snakeListAfter,(i,j),MovementUtils.CompareCoordinates)):
				line.append(0)
				total_zeros = total_zeros+1
			else:
				line.append(1)
				onlyHas0 = False
		world.append(line)
	if onlyHas0:
		return True
	visited = set()
	stack = [(x,y)]
	while stack:
		i, j = stack.pop()

		if (i, j) in visited:
			continue

		visited.add((i, j))

		# Voisins : haut, bas, gauche, droite
		voisins = [
			(i - 1, j),
			(i + 1, j),
			(i, j - 1),
			(i, j + 1)
		]

		for x, y in voisins:
			if 0 <= x < get_world_size() and 0 <= y < get_world_size():
				if world[x][y] == 0 and (x, y) not in visited:
					stack.append((x, y))

	return len(visited) == total_zeros

	

def FindNextTilePathToApple(next_x,next_y,snakeList):
	_x = get_pos_x()
	_y = get_pos_y()
	dif_x = next_x-_x
	dif_y = next_y-_y
	isNextOk = False
	dirX = East
	dirY = North
	x = 0
	y = 0
	if dif_x < 0:
		dirX = West
	else:
		dirX = East
	if dif_y < 0:
		dirY = South
	else:
		dirY = North
	while not(isNextOk):
		#Check dirX
		if dirX == West and can_move(West) and abs(dif_x)>0:
			x = _x-1
			y = _y
			snakeListAfter = AfterMoveList(snakeList,x,y)
			if VerifyMove(x,y,snakeListAfter):
				return x, y
		if dirY == South and can_move(South) and abs(dif_y)>0:
			x = _x
			y = _y-1
			snakeListAfter = AfterMoveList(snakeList,x,y)
			if VerifyMove(x,y,snakeListAfter):
				return x, y
		if dirX == East and can_move(East)  and abs(dif_x)>0:
			x = _x+1
			y = _y
			snakeListAfter = AfterMoveList(snakeList,x,y)
			if VerifyMove(x,y,snakeListAfter):
				return x, y
		if dirY == North and can_move(North) and abs(dif_y)>0:
			x = _x
			y = _y+1
			snakeListAfter = AfterMoveList(snakeList,x,y)
			if VerifyMove(x,y,snakeListAfter):
				return x, y
		#Sauvetage
		if can_move(West):
			x = _x-1
			y = _y
			snakeListAfter = AfterMoveList(snakeList,x,y)
			if VerifyMove(x,y,snakeListAfter):
				return x, y
		if can_move(South):
			x = _x
			y = _y-1
			snakeListAfter = AfterMoveList(snakeList,x,y)
			if VerifyMove(x,y,snakeListAfter):
				return x, y
		if can_move(East):
			x = _x+1
			y = _y
			snakeListAfter = AfterMoveList(snakeList,x,y)
			if VerifyMove(x,y,snakeListAfter):
				return x, y
		if can_move(North):
			x = _x
			y = _y+1
			snakeListAfter = AfterMoveList(snakeList,x,y)
			if VerifyMove(x,y,snakeListAfter):
				return x, y


def Snake():
	snakeList = []
	next_x, next_y = InitSnake()
	new_x,new_y = -1, -1
	direction = North
	firstMoveDone = False
	while(True):
		if not(can_move(East)) and not(can_move(West)) and not(can_move(North)) and not(can_move(South)) :
			InitSnake()
		isAtPosition = False
		while not(isAtPosition):
			#bouge vers la pomme
			x = get_pos_x()
			y = get_pos_y()
			new_x,new_y = FindNextTilePathToApple(next_x,next_y,snakeList)
			MovementUtils.MoveToBase(new_x,new_y)
			snakeList.append((new_x,new_y))
			if not(firstMoveDone):
				firstMoveDone = True
			else:
				snakeList.pop(0)
			if x-new_x<0:
				direction = East
			if x-new_x>0:
				direction = West
			if y-new_y<0:
				direction = North
			if y-new_y>0:
				direction = South
			isAtPosition = get_pos_x() == next_x and get_pos_y() == next_y 
		snakeList.append((x, y))
		next_x, next_y = measure()

def HeuristicSnakeNoBrainer(worldSize):
	clear()
	set_world_size(worldSize)
	InitSnake()
	while True:
		if not(can_move(East)) and not(can_move(West)) and not(can_move(North)) and not(can_move(South)) :
			InitSnake()
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if get_pos_x()==get_world_size()-1 and get_pos_y() ==0:
					break
				if i==0:
					if i%2==0:
						move(North)
					else:
						move(South)
				else:
					if j>1 and i<get_world_size()-1 :
						if i%2==0 and j < get_world_size():
							move(North)
						if i%2==1 and j < get_world_size():
							move(South)
			move(East)
		MovementUtils.MoveToBase(0,0)

