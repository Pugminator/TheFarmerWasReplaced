import PlanterUtils
import MovementUtils
import HarvesterUtils

### TRI BULLLE ###### TRI BULLLE ###### TRI BULLLE ###### TRI BULLLE ###### TRI BULLLE ###### TRI BULLLE ###  
# Retourne une ligne de cactus et retourne le tableau de valeur, reviens à sa position initiale
def ReadLine():
	line = []
	for i in range(get_world_size()):
		line.append(measure())
		move(East)
	return line

# Tri bulle ligne
def TriLine(line):
	for i in range(get_world_size()-1,0,-1):
		for j in range(i):			
			if measure(East)<measure():
				swap(East)
			move(East)
		MovementUtils.MoveTo(0,get_pos_y())

def ParallelSortAllLinesSub(numberLine):
	for i in range(numberLine):
		line = ReadLine()
		TriLine(line)
		move(North)
		
def ParallelSortAllLines():
	worldSize = get_world_size()
	maxDrones = max_drones()
	numberLineByDrone = worldSize // maxDrones
	if (numberLineByDrone - worldSize/maxDrones) < 0:
		numberLineByDrone = numberLineByDrone +1	
	numberDrone = worldSize // numberLineByDrone
	droneList = []
	for i in range(numberDrone-1):
		droneList.append(spawn_drone(ParallelSortAllLinesSub, numberLineByDrone))
		for i in range(numberLineByDrone):
			move(North)		
	ParallelSortAllLinesSub(numberLineByDrone)
	droneHaveAllFinished = False
	while not(droneHaveAllFinished):
		droneHaveAllFinished = True
		for i in range(len(droneList)):
			if(not(has_finished(droneList[i]))):
				droneHaveAllFinished = False

# Retourne une colonne de cactus et retourne le tableau de valeur, reviens à sa position initiale
def ReadColumn():
	column = []
	for i in range(get_world_size()):
		column.append(measure())
		move(North)
	return column

# Tri bulle colonne
def TriColumn(column):
	for i in range(get_world_size()-1,0,-1):
		for j in range(i):			
			if measure(North)<measure():
				swap(North)
			move(North)
		MovementUtils.MoveTo(get_pos_x(),0)

def ParallelSortAllColumnsSub(numberLine):
	for i in range(numberLine):
		column = ReadColumn()
		TriColumn(column)
		move(East)

def ParallelSortAllColumns():
	worldSize = get_world_size()
	maxDrones = max_drones()
	numberLineByDrone = worldSize // maxDrones
	if (numberLineByDrone - worldSize/maxDrones) < 0:
		numberLineByDrone = numberLineByDrone +1	
	numberDrone = worldSize // numberLineByDrone
	droneList = []
	for i in range(numberDrone-1):
		droneList.append(spawn_drone(ParallelSortAllColumnsSub, numberLineByDrone))
		for i in range(numberLineByDrone):
			move(East)		
	ParallelSortAllColumnsSub(numberLineByDrone)
	droneHaveAllFinished = False
	while not(droneHaveAllFinished):
		droneHaveAllFinished = True
		for i in range(len(droneList)):
			if(not(has_finished(droneList[i]))):
				droneHaveAllFinished = False

def FullCactusTriBulle():
	clear()
	PlanterUtils.ParallelPlantAllMapWith(Entities.Cactus)
	MovementUtils.MoveTo(0,0)
	ParallelSortAllLines()
	MovementUtils.MoveTo(0,0)
	ParallelSortAllColumns()
	HarvesterUtils.HarvestTileOfEntity(Entities.Cactus)

### TRI BULLLE ###### TRI BULLLE ###### TRI BULLLE ###### TRI BULLLE ###### TRI BULLLE ###### TRI BULLLE ###  
