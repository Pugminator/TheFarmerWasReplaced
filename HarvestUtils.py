import PlanterUtils
### Fonctions de recolte ###
# Récolte toute la carte sans se soucier du type de plante
def HarvestAllMap():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			HarvestTile()
			move(East)			
		move(North)

# Récolte une case sans se soucier du type de plante
def HarvestTile():
	if(can_harvest()):
		harvest()
		
# Recolte la tuile uniquement si de type Entity
def HarvestTileOfEntity(Entity):
	if(get_entity_type() == Entity):
		HarvestTile()
		
# Récolte toute les plante de type Entity sur la carte (1 drone unique)
def HarvestAllMapOfEntity(Entity):
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			HarvestTileOfEntity(Entity)
			move(East)			
		move(North)
		
# Recolte toute la carte avec une entité (parallelisme)
def ParallelHarvestAllMapWith(Entity):
	worldSize = get_world_size()
	maxDrones = max_drones()
	numberLineByDrone = worldSize // maxDrones
	if (numberLineByDrone - worldSize/maxDrones) < 0:
		numberLineByDrone = numberLineByDrone +1	
	numberDrone = worldSize // numberLineByDrone
	for i in range(numberDrone-1):
		spawn_drone(ParallelHarvestAllMapWithLine, numberLineByDrone, Entity)
		for i in range(numberLineByDrone):
			move(North)		
	ParallelHarvestAllMapWithLine(numberLineByDrone,Entity)
			
def ParallelHarvestAllMapWithLine(numberLine, Entity):
	for i in range(numberLine):
		for j in range(get_world_size()):
			HarvestTileOfEntity(Entity)
			if j < get_world_size()-1:	
				move(East)
		if i < numberLine-1:	
			move(North)		
			
# Recolte toute la carte avec une entité en replantant (parallelisme)
def ParallelHarvestReplantAllMapWith(Entity):
	worldSize = get_world_size()
	maxDrones = max_drones()
	numberLineByDrone = worldSize // maxDrones
	if (numberLineByDrone - worldSize/maxDrones) < 0:
		numberLineByDrone = numberLineByDrone +1	
	numberDrone = worldSize // numberLineByDrone
	for i in range(numberDrone-1):
		spawn_drone(ParallelHarvestReplantAllMapWithLine, numberLineByDrone, Entity)
		for i in range(numberLineByDrone):
			move(North)		
	ParallelHarvestReplantAllMapWithLine(numberLineByDrone,Entity)
			
def ParallelHarvestReplantAllMapWithLine(numberLine, Entity):
	while True:
		for i in range(numberLine):
			for j in range(get_world_size()):
				HarvestTileOfEntity(Entity)
				if(Entity == Entities.Tree):
					if((get_pos_y()+j)%2==0):
						PlanterUtils.PlantEntity(Entity)
					if((get_pos_y()+j)%2==1): 
						PlanterUtils.PlantEntity(Entities.Bush)
				else:	
					PlanterUtils.PlantEntity(Entity)
				if j < get_world_size()-1:	
					move(East)
			if i < numberLine-1:	
				move(North)		

				