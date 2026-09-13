import MovementUtils
import PlanterUtils
import HarvesterUtils

def GetWood():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if (i+j)%2 == 0:
				PlanterUtils.PlantEntity(Entities.Bush)
			else:
				PlanterUtils.PlantEntity(Entities.Tree)
			if(num_items(Items.Water)>0 and get_water()<0.75):
				use_item(Items.Water)
			move(North)
		move(East)
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			harvest()
			move(North)
		move(East)

def DoPolyculture3x3(Entity):
	init_x = get_pos_x()
	init_y = get_pos_y()
	dict = {}
	for i in range(init_x-3,init_x+4):
		for j in range(init_y-3,init_y+4):
			dict[((i+get_world_size())%get_world_size(),(j+get_world_size())%get_world_size())]=Entity
	while num_items(Items.Hay) < 100000000:
		MovementUtils.MoveTo(init_x,init_y)
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

clear()
GetWood()
while num_items(Items.Hay) < 100000000:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			DoPolyculture3x3(Entities.Grass)
			move(North)
		move(East)