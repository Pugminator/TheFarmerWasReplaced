def CreateLabyrinth():
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)

def ForceBrute():
	lastMove = East
	while True:
		x = get_pos_x()
		y = get_pos_y()
		hasMove = False
		if(lastMove == East):
			move(South)
			if(get_pos_x() == x and get_pos_y() == y):
				move(East)
				if(get_pos_x() == x and get_pos_y() == y):
					move(North)
					if(get_pos_x() == x and get_pos_y() == y):
						move(West)
						lastMove = West
						hasMove = True
					else:
						lastMove = North
						hasMove = True
				else:
					lastMove = East
					hasMove = True
			else:
				lastMove = South
				hasMove = True
		
		if(lastMove == North and hasMove==False):
			move(East)
			if(get_pos_x() == x and get_pos_y() == y):
				move(North)
				if(get_pos_x() == x and get_pos_y() == y):
					move(West)
					if(get_pos_x() == x and get_pos_y() == y):
						move(South)
						lastMove = South
						hasMove = True		
					else:
						lastMove = West
						hasMove = True
				else:
					lastMove = North
					hasMove = True
			else:
				lastMove = East
				hasMove = True
				
		if(lastMove == West and hasMove==False):
			move(North)
			if(get_pos_x() == x and get_pos_y() == y):
				move(West)
				if(get_pos_x() == x and get_pos_y() == y):
					move(South)
					if(get_pos_x() == x and get_pos_y() == y):
						move(East)
						lastMove = East
						hasMove = True		
					else:
						lastMove = South
						hasMove = True
				else:
					lastMove = West
					hasMove = True
			else:
				lastMove = North
				hasMove = True
		
		if(lastMove == South and hasMove==False):
			move(West)
			if(get_pos_x() == x and get_pos_y() == y):
				move(South)
				if(get_pos_x() == x and get_pos_y() == y):
					move(East)
					if(get_pos_x() == x and get_pos_y() == y):
						move(North)
						lastMove = North
						hasMove = True		
					else:
						lastMove = East
						hasMove = True
				else:
					lastMove = South
					hasMove = True
			else:
				lastMove = West
				hasMove = True
		
		
		if get_entity_type() == Entities.Grass:
			break				
		if get_entity_type() == Entities.Treasure:
			harvest()
			break	

def ForceBruteLeft():
	lastMove = West
	while True:
		x = get_pos_x()
		y = get_pos_y()
		hasMove = False
		if(lastMove == West):
			move(South)
			if(get_pos_x() == x and get_pos_y() == y):
				move(West)
				if(get_pos_x() == x and get_pos_y() == y):
					move(North)
					if(get_pos_x() == x and get_pos_y() == y):
						move(East)
						lastMove = East
						hasMove = True
					else:
						lastMove = North
						hasMove = True
				else:
					lastMove = West
					hasMove = True
			else:
				lastMove = South
				hasMove = True
				
		if(lastMove == South and hasMove==False):
			move(East)
			if(get_pos_x() == x and get_pos_y() == y):
				move(South)
				if(get_pos_x() == x and get_pos_y() == y):
					move(West)
					if(get_pos_x() == x and get_pos_y() == y):
						move(North)
						lastMove = North
						hasMove = True
					else:
						lastMove = West
						hasMove = True
				else:
					lastMove = South
					hasMove = True
			else:
				lastMove = East
				hasMove = True
		
		if(lastMove == East and hasMove==False):
			move(North)
			if(get_pos_x() == x and get_pos_y() == y):
				move(East)
				if(get_pos_x() == x and get_pos_y() == y):
					move(South)
					if(get_pos_x() == x and get_pos_y() == y):
						move(West)
						lastMove = West
						hasMove = True
					else:
						lastMove = South
						hasMove = True
				else:
					lastMove = East
					hasMove = True
			else:
				lastMove = North
				hasMove = True

		if(lastMove == North and hasMove==False):
			move(West)
			if(get_pos_x() == x and get_pos_y() == y):
				move(North)
				if(get_pos_x() == x and get_pos_y() == y):
					move(East)
					if(get_pos_x() == x and get_pos_y() == y):
						move(South)
						lastMove = South
						hasMove = True
					else:
						lastMove = East
						hasMove = True
				else:
					lastMove = North
					hasMove = True
			else:
				lastMove = West
				hasMove = True
						
		if get_entity_type() == Entities.Grass:
			break	
		if get_entity_type() == Entities.Treasure:
			harvest()
			break

def HasMoreThanOnePosibilities(lastMove):
	possibilitiesCount = 0
	if can_move(North) and lastMove != South:
		possibilitiesCount = possibilitiesCount +1
	if can_move(East) and lastMove != West:
		possibilitiesCount = possibilitiesCount +1
	if can_move(South) and lastMove != North:
		possibilitiesCount = possibilitiesCount +1
	if can_move(West) and lastMove != East:
		possibilitiesCount = possibilitiesCount +1
	return possibilitiesCount>1
		
def ForceBruteWithDrone(lastMove, firstSpawn):
	#lastMove = East
	while True:
		x = get_pos_x()
		y = get_pos_y()
		hasMove = False				
		if HasMoreThanOnePosibilities(lastMove) and num_drones()<max_drones() and firstSpawn == False:
			spawn_drone(ForceBruteLeftWithDrone,lastMove,True)
		firstSpawn = False
		if(lastMove == East):
			move(South)
			if(get_pos_x() == x and get_pos_y() == y):
				move(East)
				if(get_pos_x() == x and get_pos_y() == y):
					move(North)
					if(get_pos_x() == x and get_pos_y() == y):
						move(West)
						lastMove = West
						hasMove = True
					else:
						lastMove = North
						hasMove = True
				else:
					lastMove = East
					hasMove = True
			else:
				lastMove = South
				hasMove = True
		
		if(lastMove == North and hasMove==False):
			move(East)
			if(get_pos_x() == x and get_pos_y() == y):
				move(North)
				if(get_pos_x() == x and get_pos_y() == y):
					move(West)
					if(get_pos_x() == x and get_pos_y() == y):
						move(South)
						lastMove = South
						hasMove = True		
					else:
						lastMove = West
						hasMove = True
				else:
					lastMove = North
					hasMove = True
			else:
				lastMove = East
				hasMove = True
				
		if(lastMove == West and hasMove==False):
			move(North)
			if(get_pos_x() == x and get_pos_y() == y):
				move(West)
				if(get_pos_x() == x and get_pos_y() == y):
					move(South)
					if(get_pos_x() == x and get_pos_y() == y):
						move(East)
						lastMove = East
						hasMove = True		
					else:
						lastMove = South
						hasMove = True
				else:
					lastMove = West
					hasMove = True
			else:
				lastMove = North
				hasMove = True
		
		if(lastMove == South and hasMove==False):
			move(West)
			if(get_pos_x() == x and get_pos_y() == y):
				move(South)
				if(get_pos_x() == x and get_pos_y() == y):
					move(East)
					if(get_pos_x() == x and get_pos_y() == y):
						move(North)
						lastMove = North
						hasMove = True		
					else:
						lastMove = East
						hasMove = True
				else:
					lastMove = South
					hasMove = True
			else:
				lastMove = West
				hasMove = True
		
		
		if get_entity_type() == Entities.Grass:
			break				
		if get_entity_type() == Entities.Treasure:
			harvest()
			break


		
def ForceBruteLeftWithDrone(lastMove, firstSpawn):
	#lastMove = West
	while True:
		x = get_pos_x()
		y = get_pos_y()
		hasMove = False				
		if HasMoreThanOnePosibilities(lastMove) and num_drones()<max_drones() and firstSpawn == False:
			spawn_drone(ForceBruteWithDrone,lastMove,True)
		firstSpawn = False
		if(lastMove == West):
			move(South)
			if(get_pos_x() == x and get_pos_y() == y):
				move(West)
				if(get_pos_x() == x and get_pos_y() == y):
					move(North)
					if(get_pos_x() == x and get_pos_y() == y):
						move(East)
						lastMove = East
						hasMove = True
					else:
						lastMove = North
						hasMove = True
				else:
					lastMove = West
					hasMove = True
			else:
				lastMove = South
				hasMove = True
				
		if(lastMove == South and hasMove==False):
			move(East)
			if(get_pos_x() == x and get_pos_y() == y):
				move(South)
				if(get_pos_x() == x and get_pos_y() == y):
					move(West)
					if(get_pos_x() == x and get_pos_y() == y):
						move(North)
						lastMove = North
						hasMove = True
					else:
						lastMove = West
						hasMove = True
				else:
					lastMove = South
					hasMove = True
			else:
				lastMove = East
				hasMove = True
		
		if(lastMove == East and hasMove==False):
			move(North)
			if(get_pos_x() == x and get_pos_y() == y):
				move(East)
				if(get_pos_x() == x and get_pos_y() == y):
					move(South)
					if(get_pos_x() == x and get_pos_y() == y):
						move(West)
						lastMove = West
						hasMove = True
					else:
						lastMove = South
						hasMove = True
				else:
					lastMove = East
					hasMove = True
			else:
				lastMove = North
				hasMove = True

		if(lastMove == North and hasMove==False):
			move(West)
			if(get_pos_x() == x and get_pos_y() == y):
				move(North)
				if(get_pos_x() == x and get_pos_y() == y):
					move(East)
					if(get_pos_x() == x and get_pos_y() == y):
						move(South)
						lastMove = South
						hasMove = True
					else:
						lastMove = East
						hasMove = True
				else:
					lastMove = North
					hasMove = True
			else:
				lastMove = West
				hasMove = True
						
		if get_entity_type() == Entities.Grass:
			break	
		if get_entity_type() == Entities.Treasure:
			harvest()
			break


def DefaultResolve():
	clear()
	while True:
		CreateLabyrinth()
		spawn_drone(ForceBrute)
		ForceBruteLeft()
		
def DroneResolve():
	clear()
	while True:
		CreateLabyrinth()
		ForceBruteWithDrone(East, False)
		
		
DroneResolve() 