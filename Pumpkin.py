import PlanterUtils
import MovementUtils
import HarvesterUtils

# Crée une giga citrouille
def GrowMegaPumpkin():
	clear()
	PlanterUtils.ParallelPlantAllMapWith(Entities.Pumpkin)
	MovementUtils.MoveTo(0,0)
	ParallelCheckLine()
	MovementUtils.MoveTo(0,0)
	HarvesterUtils.HarvestTileOfEntity(Entities.Pumpkin)

def ParallelCheckLineSub(numberLine):
	origin_y = get_pos_y()
	IsPumpkinFullyGrown = False
	while not(IsPumpkinFullyGrown):
		PumpkinNumberLineOK = 0
		MovementUtils.MoveTo(0,origin_y)
		for i in range(numberLine):			
			PumpkinNumber = 0
			for j in range(get_world_size()):
				if get_entity_type() == Entities.Dead_Pumpkin:
					PlanterUtils.PlantPumpkin()
					PumpkinNumber = 0
				elif get_entity_type() == Entities.Pumpkin and can_harvest():
					PumpkinNumber = PumpkinNumber + 1	
				move(East)
			move(North)
			if PumpkinNumber == get_world_size():
				PumpkinNumberLineOK = PumpkinNumberLineOK +1
		if PumpkinNumberLineOK == numberLine:
			IsPumpkinFullyGrown = True
			
		
def ParallelCheckLine():
	worldSize = get_world_size()
	maxDrones = max_drones()
	numberLineByDrone = worldSize // maxDrones
	if (numberLineByDrone - worldSize/maxDrones) < 0:
		numberLineByDrone = numberLineByDrone +1	
	numberDrone = worldSize // numberLineByDrone
	droneList = []
	for i in range(numberDrone-1):
		droneList.append(spawn_drone(ParallelCheckLineSub, numberLineByDrone))
		for i in range(numberLineByDrone):
			move(North)
	ParallelCheckLineSub(numberLineByDrone)
	droneHaveAllFinished = False
	while not(droneHaveAllFinished):
		droneHaveAllFinished = True
		for i in range(len(droneList)):
			if(not(has_finished(droneList[i]))):
				droneHaveAllFinished = False				
			