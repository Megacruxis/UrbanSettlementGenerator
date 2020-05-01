def generateCentralTable(world, y, x, z, stair_id):
	world.setValue(y+1, x, z, (85,0))
	world.setValue(y+2, x, z, (72,0))
	world.setValue(y+1, x-1, z, (stair_id, 1))
	world.setValue(y+1, x+1, z, (stair_id, 0))

def generateCentralTableSouth(world, y, x, z, stair_id):
	world.setValue(y+1, x, z, (85,0))
	world.setValue(y+2, x, z, (72,0))
	world.setValue(y+1, x, z-1, (stair_id, 3))
	world.setValue(y+1, x, z+1, (stair_id, 2))

def generateBookshelf(world, y, x, z):
	world.setValue(y+1, x-1, z-1, (47,0))
	world.setValue(y+1, x-2, z-1, (47,0))
	world.setValue(y+2, x-1, z-1, (47,0))
	world.setValue(y+2, x-2, z-1, (47,0))
	world.setValue(y+3, x-1, z-1, (126, 0))
	world.setValue(y+3, x-2, z-1, (126, 0))

def generateBookshelfEast(world, y, x, z):
	world.setValue(y+1, x-1, z-1, (47,0))
	world.setValue(y+1, x-1, z-2, (47,0))
	world.setValue(y+2, x-1, z-1, (47,0))
	world.setValue(y+2, x-1, z-2, (47,0))
	world.setValue(y+3, x-1, z-1, (126, 0))
	world.setValue(y+3, x-1, z-2, (126, 0))

def generateCouch(world, y, x, z, stair_id):
	world.setValue(y+1, x+3, z-1, (stair_id, 0))
	world.setValue(y+1, x+2, z-1, (stair_id, 2))
	world.setValue(y+1, x+1, z-1, (stair_id, 1))

def generateChandelier(world, y, x, z, fence_id, size=1):
	for i in range(1, size+1):
		world.setValue(y-i, x, z, fence_id)
	else:
		world.setValue(y-i-1, x, z, (169,0))

def generateBed(world, y, x, z):
	world.setEntity(y+1, x-1, z+1, (26,11), "bed")
	world.setEntity(y+1, x-2, z+1, (26,3), "bed")

def generateBedSouth(world, y, x, z):
	world.setEntity(y+1, x, z+1, (26,2), "bed")
	world.setEntity(y+1, x, z, (26,10), "bed")

def generatePlant(matrix, y, x, z, plant_block_id, ground_block_id):
	matrix.setValue(y + 1, x, z, ground_block_id)
	matrix.setValue(y + 1, x - 1, z, (96, 14))
	matrix.setValue(y + 1, x + 1, z, (96, 15))
	matrix.setValue(y + 1, x, z - 1, (96, 12))
	matrix.setValue(y + 1, x, z + 1, (96, 13))
	matrix.setValue(y + 2, x, z, plant_block_id)
	matrix.setValue(y + 3, x, z, plant_block_id)

def generateMailbox(matrix, y, x, z, direction) :
	matrix.setValue(y + 1, x, z, (44, 8))
	if direction == "E" :
		matrix.setValue(y + 2, x, z, (158, 5))
		matrix.setValue(y + 3, x, z, (158, 5))
	elif direction == "W" :
		matrix.setValue(y + 2, x, z, (158, 4))
		matrix.setValue(y + 3, x, z, (158, 4))
	elif direction == "S" :
		matrix.setValue(y + 2, x, z, (158, 3))
		matrix.setValue(y + 3, x, z, (158, 3))
	else :
		matrix.setValue(y + 2, x, z, (158, 2))
		matrix.setValue(y + 3, x, z, (158, 2))
	matrix.setValue(y + 4, x, z, (44, 0))

def generatePotWithPlant(matrix, y, x, z, plant_id, ground_block_id):
	matrix.setValue(y + 1, x, z, (ground_block_id))
	matrix.setEntity(y + 2, x, z, (140, 0), "flower_pot")
