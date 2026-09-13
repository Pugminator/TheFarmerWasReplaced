import MovementUtils
import PlanterUtils
import HarvesterUtils
		
def PlantBush():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			plant(Entities.Bush)
			move(North)
		move(East)

PlantBush()
plant(Entities.Grass)
while num_items(Items.Hay) < 100000000:
	type_plante, (x, y) = get_companion()
	while type_plante!=Entities.Bush:
		harvest()
		type_plante, (x, y) = get_companion()
	while not(can_harvest()):
		if(num_items(Items.Water) > 0 and get_water()<0.75):
			use_item(Items.Water)
	harvest()