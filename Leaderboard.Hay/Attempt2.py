import MovementUtils
import PlanterUtils
import HarvesterUtils

def NoBrainer(Entity):
	clear()
	worldSize = get_world_size()
	maxDrones = max_drones()
	numberOfDronesPossible = get_world_size()**2 // 27
	droneList = []
	numberDrone = min(maxDrones,numberOfDronesPossible)
	for i in range(numberDrone-1):		
		droneList.append(spawn_drone(DoPolyculture3x3,Entity))
		move(East)
		move(East)
		move(East)
		move(East)
		move(North)
		move(North)
		move(North)
	DoPolyculture3x3(Entity)

def CanCleanNeighbour(dict,init_x,init_y):
	if(dict[((init_x+1+get_world_size())%get_world_size(),(init_y+get_world_size())%get_world_size())]!=Entities.Bush):
		return True, ((init_x+1+get_world_size())%get_world_size(),(init_y+get_world_size())%get_world_size())
	if(dict[((init_x-1+get_world_size())%get_world_size(),(init_y+get_world_size())%get_world_size())]!=Entities.Bush):
		return True, ((init_x-1+get_world_size())%get_world_size(),(init_y+get_world_size())%get_world_size())
	if(dict[((init_x+get_world_size())%get_world_size(),(init_y+1+get_world_size())%get_world_size())]!=Entities.Bush):
		return True, ((init_x+get_world_size())%get_world_size(),(init_y+1+get_world_size())%get_world_size())
	if(dict[((init_x+get_world_size())%get_world_size(),(init_y-1+get_world_size())%get_world_size())]!=Entities.Bush):
		return True, ((init_x+get_world_size())%get_world_size(),(init_y-1+get_world_size())%get_world_size())
	return False, (0,0)

def DoPolyculture3x3(Entity):
	init_x = get_pos_x()
	init_y = get_pos_y()
	dict = {}
	for i in range(init_x-3,init_x+4):
		for j in range(init_y-3,init_y+4):
			dict[((i+get_world_size())%get_world_size(),(j+get_world_size())%get_world_size())]=Entity
	while num_items(Items.Hay) < 2000000000:
		MovementUtils.MoveTo(init_x,init_y)
		PlanterUtils.PlantEntity(Entity)
		type_plante, (x, y) = get_companion()
		if(dict[(x, y)] != type_plante):
			MovementUtils.MoveTo(x,y)
			PlanterUtils.PlantEntity(type_plante)
			dict[(x,y)] = type_plante
			MovementUtils.MoveTo(init_x,init_y)
		while not(can_harvest()):
			if(num_items(Items.Water) > 0 and get_water()<0.75):
				use_item(Items.Water)
		harvest()

HarvesterUtils.ParallelHarvestAllMapWith(Entities.Grass)
MovementUtils.MoveTo(0,0)		
PlanterUtils.ParallelPlantAllMapWith(Entities.Tree)
MovementUtils.MoveTo(0,0)
HarvesterUtils.ParallelHarvestAllMapWith(Entities.Tree)
MovementUtils.MoveTo(0,0)
PlanterUtils.ParallelPlantAllMapWith(Entities.Carrot)
MovementUtils.MoveTo(0,0)
HarvesterUtils.ParallelHarvestAllMapWith(Entities.Carrot)
MovementUtils.MoveTo(0,0)
NoBrainer(Entities.Grass)