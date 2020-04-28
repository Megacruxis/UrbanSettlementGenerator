import random
import math
import RNG
import logging
from pymclevel import alphaMaterials, BoundingBox
import utilityFunctions as utilityFunctions
from GenerateObject import *
from GenerateCarpet import generateCarpet

def generateBuilding(matrix, h_min, h_max, x_min, x_max, z_min, z_max):

	building = utilityFunctions.dotdict()
	building.type = "building"

	building.area = utilityFunctions.dotdict({"y_min": h_min, "y_max": h_max, "x_min": x_min, "x_max": x_max, "z_min": z_min, "z_max": z_max})

	utilityFunctions.cleanProperty(matrix, h_min+1, h_max, x_min, x_max, z_min, z_max)

	(h_min, h_max, x_min, x_max, z_min, z_max) = getBuildingAreaInsideLot(h_min, h_max, x_min, x_max, z_min, z_max)
	building.constructionArea = (h_min, h_max, x_min, x_max, z_min, z_max)

	logging.info("Generating house at area {}".format(building.area))
	logging.info("Construction area {}".format(building.constructionArea))

	wall = (159, random.randint(0,15))
	ceiling = wall
	floor = wall

	floor_size = 8
	max_height = h_max-h_min
	if max_height > 32:
		h_max = h_min+random.randint(32, 80 if max_height > 80 else max_height)

	while (h_max-h_min) % floor_size != 0:
		h_max -= 1

	generateBuildingWalls(matrix, h_min, h_max, floor_size, x_min, x_max, z_min, z_max, wall)
	generateFloorsDivision(matrix, h_min, h_max, floor_size, x_min, x_max, z_min, z_max, wall)

	building.orientation = getOrientation()

	if building.orientation == "S":
		door_x = RNG.randint(x_min+1, x_max-1)
		door_z = z_max
		generateDoor(matrix, h_min+1, door_x, door_z, (64,9), (64,3))
		building.entranceLot = (h_min+1, door_x, building.area.z_max)
		for z in range(door_z+1, building.area.z_max):
			matrix.setValue(h_min,door_x,z, (4,0))
			matrix.setValue(h_min,door_x-1,z, (4,0))
			matrix.setValue(h_min,door_x+1,z, (4,0))
		# determine which floor have two apartment instead of one
		double_apartment_floor = pickDoubleapartmentFloor(h_min, h_max, floor_size)
		# apartment windows
		generateBuildingWindows_AlongZ(matrix, h_min, h_max, floor_size, x_min, x_max, z_min, double_apartment_floor)
		# corridor windows
		generateBuildingWindows_AlongZ(matrix, h_min, h_max, floor_size, x_min, x_max, z_max, [])
		generateCorridorInterior(matrix, h_min, h_max, floor_size, x_min, x_max, z_max-6, z_max)
		generateFloorPlan(matrix, h_min, h_max, floor_size, x_min, x_max, z_min, z_max, wall, double_apartment_floor)

		generateStairs(matrix, h_min, h_max, floor_size, x_min, x_max, z_min, z_max, wall)
		generateApartmentInterior(matrix, h_min, h_max, floor_size, x_min, x_max, z_min, z_max-6, double_apartment_floor)

	return (building, h_max / floor_size)

def getBuildingAreaInsideLot(h_min, h_max, x_min, x_max, z_min, z_max):
	building_size_x = random.randint(15, 18)
	if x_max-x_min > building_size_x:
		x_mid = x_min + (x_max-x_min)/2
		x_min = x_mid - building_size_x/2
		x_max = x_mid + building_size_x/2

	building_size_z = random.randint(15, 18)
	if z_max-z_min > building_size_z:
		z_mid = z_min + (z_max-z_min)/2
		z_min = z_mid - building_size_z/2
		z_max = z_mid + building_size_z/2

	return (h_min, h_max, x_min, x_max, z_min, z_max)

def pickDoubleapartmentFloor(h_min, h_max, floor_size):
	floor_number = (h_max - h_min) / floor_size
	picked_number = random.randint(0, floor_number - 1)
	double_apartment_floor = []
	floors = []
	for i in range(1, floor_number) :
		floors.append(i)
	#logging.info("################")
	#logging.info("picking {} floors out of {}".format(picked_number, floor_number))
	while picked_number > 0 :
		picked_floor = floors[random.randint(0, len(floors)-1)]
		double_apartment_floor.append(picked_floor * floor_size + h_min)
		floors.remove(picked_floor)
		picked_number -= 1

	return double_apartment_floor

def generateStairs(matrix, h_min, h_max, floor_size, x_min, x_max, z_min, z_max, wall):
	cur_floor = h_min
	floor = 0
	while cur_floor < h_max-floor_size:
		step = cur_floor+floor_size-1
		if floor % 2 == 0:
			x = x_max-2
			z = z_max-2
			for x1 in range(x, x-3, -1):
				#removes the floor blocks
				matrix.setValue(step+1, x1, z, (0, 0))
				matrix.setValue(step+1, x1, z-1, (0, 0))
				#removes the carpet blocks
				matrix.setValue(step+2, x1, z, (0, 0))
				matrix.setValue(step+2, x1, z-1, (0, 0))

			while step > cur_floor:
				matrix.setValue(step, x, z, (109, 0))
				matrix.setValue(step, x, z-1, (109, 0))
				for h in range(cur_floor+1, step):
					matrix.setValue(h, x, z, (98, 0))
					matrix.setValue(h, x, z-1, (98, 0))

				step -= 1
				x -= 1
		if floor % 2 == 1:
			x = x_min+2
			z = z_max-2
			for x1 in range(x, x+3):
				#removes the floor blocks
				matrix.setValue(step+1, x1, z, (0, 0))
				matrix.setValue(step+1, x1, z-1, (0, 0))
				#removes the carpet blocks
				matrix.setValue(step+2, x1, z, (0, 0))
				matrix.setValue(step+2, x1, z-1, (0, 0))
			while step > cur_floor:
				matrix.setValue(step, x, z, (109, 1))
				matrix.setValue(step, x, z-1, (109, 1))
				for h in range(cur_floor+1, step):
					matrix.setValue(h, x, z, (98, 0))
					matrix.setValue(h, x, z-1, (98, 0))
				step -= 1
				x += 1

		floor += 1
		cur_floor += floor_size

def generateFloorPlan(matrix, h_min, h_max, floor_size, x_min, x_max, z_min, z_max, wall, double_apartment_floor):
	cur_floor = h_min
	z_wall = z_max-6

	while cur_floor < h_max:

		# generating separating wall between hall and apartments
		for h in range(cur_floor, cur_floor+floor_size):
			for x in range(x_min, x_max):
				matrix.setValue(h, x, z_wall, wall)
		if cur_floor in double_apartment_floor :
			# generating separating wall between the two apartments
			x_mid = x_max - (x_max - x_min) / 2
			for h in range(cur_floor, cur_floor+floor_size):
				for z in range(z_min+1, z_wall):
					matrix.setValue(h, x_mid, z, wall)
			# generating door to both apartment
			bonus = 1 if (x_mid - x_min) / 2 < 4 else 0
			generateDoor(matrix, cur_floor+1, x_mid + (x_mid - x_min) / 2 + bonus, z_wall, (64,8), (64,3))
			generateDoor(matrix, cur_floor+1, x_mid - (x_mid - x_min) / 2, z_wall, (64,9), (64,3))
		else :
			# generating door to the apartment
			x_door = x_max - ((x_max-x_min)/2)
			generateDoor(matrix, cur_floor+1, x_door, z_wall, (64,9), (64,3))

		cur_floor += floor_size

def generateApartmentInterior(matrix, h_min, h_max, floor_size, x_min, x_max, z_min, z_max, double_apartment_floor):
	#z_max = z_max -6
	cur_floor = h_min
	floor = 0
	x_mid = x_max - int((x_max - x_min)/2)
	z_mid = z_max - int((z_max - z_min)/2)

	while cur_floor < h_max:
		cur_floor_ceiling = cur_floor+floor_size
		if cur_floor in double_apartment_floor :
			#first apartment
			generateCarpet(matrix.matrix, cur_floor+1, x_min+1, x_mid, z_min+1, z_max)
			generateChandelier(matrix, cur_floor_ceiling, x_mid-4, z_mid, 2)
			generateCouch(matrix, cur_floor, x_min, z_max)
			generateBedSouth(matrix, cur_floor, x_min + 1, z_min + 1)
			generateCentralTableSouth(matrix, cur_floor, x_mid - (x_mid- x_min) / 2, z_mid)
			generateBookshelfEast(matrix, cur_floor, x_mid, z_max)
			#second apartment
			generateCarpet(matrix.matrix, cur_floor+1, x_mid+1, x_max, z_min+1, z_max)
			generateChandelier(matrix, cur_floor_ceiling, x_mid+4, z_mid, 2)
			generateCouch(matrix, cur_floor, x_mid, z_max)
			generateBedSouth(matrix, cur_floor, x_max - 1, z_min + 1)
			generateCentralTableSouth(matrix, cur_floor, x_mid + (x_mid- x_min) / 2, z_mid)
			generateBookshelfEast(matrix, cur_floor, x_max, z_max)
		else :
			generateCarpet(matrix.matrix, cur_floor+1, x_min+1, x_max, z_min+1, z_max)
			generateBed(matrix, cur_floor, x_max, z_min)
			generateCentralTable(matrix, cur_floor, x_mid, z_mid)
			generateBookshelf(matrix, cur_floor, x_max, z_max)
			generateCouch(matrix, cur_floor, x_min, z_max)

			x_mid = x_min + (x_max-x_min)/2
			z_mid = z_min + (z_max-z_min)/2
			generateChandelier(matrix, cur_floor_ceiling, x_mid-5, z_mid, 2)
			generateChandelier(matrix, cur_floor_ceiling, x_mid+5, z_mid, 2)

		cur_floor += floor_size

def generateCorridorInterior(matrix, h_min, h_max, floor_size, x_min, x_max, z_min, z_max):
	cur_floor = h_min
	floor = 0
	x_mid = x_max - int((x_max - x_min)/2)
	z_mid = z_max - int((z_max - z_min)/2)

	while cur_floor < h_max:
		cur_floor_ceiling = cur_floor+floor_size

		x_mid = x_min + (x_max-x_min)/2
		z_mid = z_min + (z_max-z_min)/2
		generateChandelier(matrix, cur_floor_ceiling, x_mid, z_mid, 1)

		# corridor's carpet
		for x in range(x_min+1, x_max):
			for z in range(z_min+1, z_max):
				matrix.setValue(cur_floor+1,x,z, (171, 12))

		cur_floor += floor_size

def generateBuildingWalls(matrix, h_min, h_max, floor_size, x_min, x_max, z_min, z_max, wall):

	# walls along x axis
	for x in range(x_min, x_max+1):
		for y in range(h_min, h_max):
			matrix.setValue(y,x,z_max, wall)
			matrix.setValue(y,x,z_min, wall)

	# walls along z axis
	for z in range(z_min, z_max+1):
		for y in range(h_min, h_max):
			matrix.setValue(y,x_max,z, wall)
			matrix.setValue(y,x_min,z, wall)

def generateFloorsDivision(matrix, h_min, h_max, floor_size, x_min, x_max, z_min, z_max, wall):
	# floors division
	cur_floor = h_min
	while cur_floor <= h_max:
		for x in range(x_min, x_max+1):
			for z in range(z_min, z_max+1):
				matrix.setValue(cur_floor,x,z, wall)

		cur_floor += floor_size

def getOrientation():
	return "S"

def generateDoor(matrix, y, x, z, door_up, door_down):
	matrix.setValue(y+1, x, z, door_up)
	matrix.setValue(y, x, z, door_down)

def constructWindows(matrix, h, x, x_shifting, z, window_id):
	matrix.setValue(h, x + x_shifting, z, window_id)
	matrix.setValue(h - 1, x + x_shifting, z, window_id)
	matrix.setValue(h, x - x_shifting, z, window_id)
	matrix.setValue(h - 1, x - x_shifting, z, window_id)

def generateBuildingWindows_AlongZ(matrix, h_min, h_max, floor_size, x_min, x_max, z, double_apartment_floor):
	x_window_size = x_max-random.randint(x_min+2, x_max-2)

	# windows
	cur_floor = h_min
	while cur_floor < h_max:
		window_h = cur_floor + 1 + int(math.ceil(floor_size/2))
		if cur_floor in double_apartment_floor :
			x_mid = x_max - (x_max - x_min)/2
			shifting = 1
			while x_mid + shifting + 1 < x_max and x_mid - shifting - 1 > x_min :
				constructWindows(matrix, window_h, x_mid, shifting, z, (20,0))
				constructWindows(matrix, window_h, x_mid, shifting + 1, z, (20,0))
				if shifting == 1 and x_mid + shifting + 2 < x_max and x_mid - shifting - 2 > x_min :
					constructWindows(matrix, window_h, x_mid, shifting + 2, z, (20,0))
					shifting += 1
				shifting += 3
		else :
			for x in range(x_min+2, x_max-1, 3):
				# apartment windows
				matrix.setValue(window_h, x, z, (20,0))
				matrix.setValue(window_h-1, x, z, (20,0))
				matrix.setValue(window_h, x+1, z, (20,0))
				matrix.setValue(window_h-1, x+1, z, (20,0))

		cur_floor += floor_size
