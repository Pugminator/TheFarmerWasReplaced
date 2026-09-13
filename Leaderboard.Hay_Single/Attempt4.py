import MovementUtils
import PlanterUtils
import HarvesterUtils
		
def PlantBush():
	for i in range(8):
		for j in range(8):
			if not(get_pos_x()==1 and get_pos_y()==0):
				plant(Entities.Bush)
			if(i%2==0):
				move(North)
			else:
				move(South)
		move(East)

PlantBush()
hasMove = False
while num_items(Items.Hay) < 100000000:
	type_plante, (x, y) = get_companion()
	while type_plante!=Entities.Bush:
		harvest()
		type_plante, (x, y) = get_companion()
	if not(can_harvest()):
		if(num_items(Items.Water) > 0 and get_water()<0.75):
			use_item(Items.Water)
		if(hasMove):
			move(West)
		else:
			move(East)
		hasMove = not(hasMove)
	else:
		harvest()