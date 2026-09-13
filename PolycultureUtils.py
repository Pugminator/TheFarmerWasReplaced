import PlanterUtils
import HarvesterUtils
import MovementUtils
import GenericUtils

# Plante l'entité companion
def PlantCompanionEntity():
	if get_entity_type() != None:
		type_plante, (x, y) = get_companion()		
		MovementUtils.MoveTo(x,y)
		PlanterUtils.PlantEntity(type_plante)
	else:
		PlanterUtils.PlantRandomPolyculture()	

def DoPolycultureCycle():
	listeCooordinates = []
	listeCooordinates.append((get_pos_x(),get_pos_y()))
	isCycling = False
	PlanterUtils.PlantRandomPolyculture()
	while not(isCycling):
		PlantCompanionEntity()
		if not(GenericUtils.Exists(listeCooordinates, (get_pos_x(),get_pos_y()), MovementUtils.CompareCoordinates)):
			listeCooordinates.append((get_pos_x(),get_pos_y()))
		else:
			isCycling = True
	for i in range(len(listeCooordinates)):
		MovementUtils.MoveTo(listeCooordinates[i][0], listeCooordinates[i][1])
		harvest()
		
# Cultive uniquement de ce materiaux (parallelisme)
def CultivateOnly(Entity):
	MovementUtils.MoveTo(0,0)
	HarvesterUtils.ParallelHarvestReplantAllMapWith(Entity)

def CultivateOnlyV2(Entity):
	HarvesterUtils.ParallelHarvestReplantAllMapWith(Entity)
	