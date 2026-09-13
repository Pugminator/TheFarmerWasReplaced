import MovementUtils
import PlanterUtils
import HarvesterUtils
		
def PlantBush():
	for i in range(7):
		for j in range(7):
			if abs(get_pos_x()-3)+abs(get_pos_y()-3)<=3:
				plant(Entities.Bush)
			if(j<6):
				if(i%2==0):
					move(North)
				else:
					move(South)
		move(East)

PlantBush()
MovementUtils.MoveTo(3,3)
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