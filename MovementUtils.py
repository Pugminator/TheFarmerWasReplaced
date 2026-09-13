### Deplacements de base #######################
# Va en distance de Manatthan au point indiqué sans se soucier des obstacles (utile pour Snake)
def MoveToBase(x,y):
	_x = get_pos_x()
	_y = get_pos_y()
	dif_x = x-_x
	dif_y = y-_y
	for i in range(abs(dif_x)):
		if dif_x < 0:
			move(West)
		else:
			move(East)
	for i in range(abs(dif_y)):
		if dif_y < 0:
			move(South)
		else:
			move(North)

# Va en distance de Manatthan au point indiqué sans se soucier des obstacles et en passant à travers les bordures si plus court
def MoveTo(x,y):
	pos_x = get_pos_x()
	pos_y = get_pos_y()
	worldSize = get_world_size()
	baseDif_x = x - pos_x
	baseDif_y = y - pos_y
	throughBorder_x = worldSize - abs(baseDif_x)
	throughBorder_y = worldSize - abs(baseDif_y)
	bestDif_x = min(abs(baseDif_x),abs(throughBorder_x))
	bestDif_y = min(abs(baseDif_y),abs(throughBorder_y))
	dir_x = East
	dir_y = North
	if bestDif_x == abs(baseDif_x):
		if baseDif_x > 0:
			dir_x = East
		else:
			dir_x = West
	else:
		if baseDif_x > 0:
			dir_x = West
		else:
			dir_x = East
	if bestDif_y == abs(baseDif_y):
		if baseDif_y > 0:
			dir_y = North
		else:
			dir_y = South
	else:
		if baseDif_y > 0:
			dir_y = South
		else:
			dir_y = North
	for i in range(abs(bestDif_x)):
		move(dir_x)
	for i in range(abs(bestDif_y)):
		move(dir_y)

def CompareCoordinates(e,x):
	return e[0] == x[0] and e[1] == x[1]
		
	