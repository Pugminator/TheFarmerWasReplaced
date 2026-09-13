### Aide generique ###################################

# Lambda fonction il existe Element dans liste telle que Compare(Element,x) = True
def Exists(Liste, Element, Compare):
	for i in range(len(Liste)):
		if Compare(Element, Liste[i]) == True:
			return True
	return False
	
# Simple fonction qui permet de placer un drone pour faire une action et de bouger en répartissant les drones equitablement
def Repartit(function):
	while num_drones() < max_drones():
		spawn_drone(function)
		for i in range(get_world_size()/max_drones()):
			move(North)