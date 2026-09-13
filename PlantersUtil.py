import GenericUtils

### Fonctions de plantations de base ########################################################################################
global Plants
Plants = [Entities.Grass, Entities.Bush, Entities.Tree, Entities.Carrot, Entities.Pumpkin, Entities.Sunflower, Entities.Cactus]
PlantsPolyculture = [Entities.Grass, Entities.Bush, Entities.Tree, Entities.Carrot]

# Garde fou avant plantation
def CanPlant(Entity):
	cost = get_cost(Entity)
	for item in cost:
		quantite = cost[item]
		if quantite >= num_items(item):
			return False
	return True	

# Plante l'entitée spécifiée
def PlantEntity(Entity):
	if Entity == Entities.Grass:
		return PlantGrass()
	elif Entity == Entities.Bush:
		return PlantBush()
	elif Entity == Entities.Tree:
		return PlantTree()
	elif Entity == Entities.Carrot:
		return PlantCarrot()
	elif Entity == Entities.Pumpkin:
		return PlantPumpkin()
	elif Entity == Entities.Sunflower:
		return PlantSunflower()
	elif Entity == Entities.Cactus:
		return PlantCactus()
	else:
		print("TODO")
		return False

# Plante une plante random
def PlantRandom():
	index = random() * len(Plants) // 1
	return PlantEntity(Plants[index])

# Plante une plante random parmis celle en polyculture
def PlantRandomPolyculture():
	index = random() * len(PlantsPolyculture) // 1
	return PlantEntity(PlantsPolyculture[index])

# Plante de l'herbe	
def PlantGrass():
	if CanPlant(Entities.Grass):
		if get_ground_type() != Grounds.Grassland:
			till()
		plant(Entities.Grass)
		return True
	return False

# Plante un buisson
def PlantBush():
	if CanPlant(Entities.Bush):
		if get_ground_type() != Grounds.Grassland:
			till()
		plant(Entities.Bush)
		return True
	return False
		
# Plante un arbre
def PlantTree():
	if CanPlant(Entities.Tree):
		if get_ground_type() != Grounds.Grassland:
			till()
		plant(Entities.Tree)
		return True
	return False

# Plante une carrotte
def PlantCarrot():
	if CanPlant(Entities.Carrot):
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Carrot)
		return True
	return False

# Plante une citrouille
def PlantPumpkin():
	if CanPlant(Entities.Pumpkin):
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Pumpkin)
		return True
	return False
		
# Plante un tournesol
def PlantSunflower():
	if CanPlant(Entities.Sunflower):
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Sunflower)
		return True
	return False
	
# Plante un cactus
def PlantCactus():
	if CanPlant(Entities.Cactus):
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Cactus)
		return True
	return False

	
### Fonctions avancées ########################################################################################
# Plantes toute la carte en aléatoire après l'avoir clear
def RandomPlantingWithClear():
	clear()
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			PlantRandom()
			move(East)			
		move(North)

# Plantes toute la carte en aléatoire
def RandomPlanting():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			PlantRandom()
			move(East)			
		move(North)
		
# Plante toute la carte avec une entité (1 drone unique)
def PlantAllMapWith(Entity):
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			PlantEntity(Entity)
			move(East)			
		move(North)	

# Plante toute la carte avec une entité (parallelisme)
def ParallelPlantAllMapWith(Entity):
	worldSize = get_world_size()
	maxDrones = max_drones()
	numberLineByDrone = worldSize // maxDrones
	if (numberLineByDrone - worldSize/maxDrones) < 0:
		numberLineByDrone = numberLineByDrone +1	
	numberDrone = worldSize // numberLineByDrone
	for i in range(numberDrone-1):
		spawn_drone(ParallelPlantAllMapWithLine, numberLineByDrone, Entity)
		for i in range(numberLineByDrone):
			move(North)		
	ParallelPlantAllMapWithLine(numberLineByDrone,Entity)
			
def ParallelPlantAllMapWithLine(numberLine, Entity):
	for i in range(numberLine):
		for j in range(get_world_size()):
			PlantEntity(Entity)
			if j < get_world_size()-1:	
				move(East)
		if i < numberLine-1:	
			move(North)			
	
	
			
