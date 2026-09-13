import MovementUtils
import PlanterUtils
import HarvesterUtils
		
def PlantBush():
	for i in range(3):
		move(North)
		plant(Entities.Bush)
	move(East)
	plant(Entities.Bush)
	for i in range(2):
		move(South)
		plant(Entities.Bush)
	move(South)
	for i in range(3):
		move(South)
		plant(Entities.Bush)
	move(East)
	for i in range(5):
		move(North)
		plant(Entities.Bush)
	move(East)
	for i in range(3):
		move(South)
		plant(Entities.Bush)
	move(East)
	move(North)
	plant(Entities.Bush)
	move(East)
	plant(Entities.Bush)
	move(South)
	move(East)
	plant(Entities.Bush)
	for i in range(2):
		move(North)
		plant(Entities.Bush)
	move(North)
	move(East)
	plant(Entities.Bush)
	for i in range(4):
		move(South)
		plant(Entities.Bush)
	move(South)
	move(East)
	plant(Entities.Bush)
	for i in range(2):
		move(North)
		plant(Entities.Bush)
	move(North)


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