import random
import math
import RNG
import logging
from pymclevel import alphaMaterials, BoundingBox
import utilityFunctions as utilityFunctions
from GenerateCarpet import generateCarpet
from GenerateObject import *

GREENHOUSE_WIDTH = 10
GREENHOUSE_DEPTH = 12
GREENHOUSE_HEIGHT = 5
DIRT_ID = (3, 0)
WHITE_GLASS_ID = (95, 0)
GLASS_ID = (20, 0)
WATER_ID = (9, 0)
SEA_LANTERN_ID = (169, 0)
PLANKS_ID = {'oak': (5, 0), 'spruce': (5, 1), 'birch': (5,2), 'jungle': (5,3), 'acacia': (5,4), 'dark_oak': (5,5)}
TRAPDOOR_ID = (96, 0)
GRASS_PATH_ID = (208, 0)
FARMLAND_ID = (60, 0)
WHEAT_ID = (59, 0)
CARROT_ID = (141, 0)
POTATO_ID = (142, 0)
plants = [WHEAT_ID, CARROT_ID, POTATO_ID]


def generateGreenhouse(matrix, h_min, h_max, x_min, x_max, z_min, z_max, usable_wood):
    greenhouse = utilityFunctions.dotdict()
    greenhouse.type = "greenhouse"
    greenhouse.lotArea = utilityFunctions.dotdict({"y_min": h_min, "y_max": h_max, "x_min": x_min, "x_max": x_max, "z_min": z_min, "z_max": z_max})

    utilityFunctions.cleanProperty(matrix, h_min+1, h_max, x_min, x_max, z_min, z_max)

    (h_min, h_max, x_min, x_max, z_min, z_max) = getGreenHouseAreaInsideLot(h_min, h_max, x_min, x_max, z_min, z_max)

    greenhouse.buildArea = utilityFunctions.dotdict({"y_min": h_min, "y_max": h_max, "x_min": x_min, "x_max": x_max, "z_min": z_min, "z_max": z_max})
    greenhouse.orientation = getOrientation()
    greenhouse.entranceLot = ( greenhouse.lotArea.y_min + 1, greenhouse.buildArea.x_min + GREENHOUSE_WIDTH / 2, greenhouse.lotArea.z_min)

    logging.info("Generating greenhouse at area {}".format(greenhouse.area))
    logging.info("Construction area {}".format(greenhouse.constructionArea))

    """Todo, Improve adaptability"""
    foundation = PLANKS_ID[usable_wood[RNG.randint(0, len(usable_wood) - 1)]]
    ground = GRASS_PATH_ID
    used_glass = WHITE_GLASS_ID

    generateGroundAndCropse(matrix, greenhouse.buildArea.y_min,greenhouse.buildArea.x_min, greenhouse.buildArea.x_max, greenhouse.buildArea.z_min, greenhouse.buildArea.z_max, foundation, ground)
    generateGlassDome(matrix, greenhouse.buildArea.y_min + 1, greenhouse.buildArea.y_min + GREENHOUSE_HEIGHT, greenhouse.buildArea.x_min, greenhouse.buildArea.x_max, greenhouse.buildArea.z_min, greenhouse.buildArea.z_max, used_glass)
    generateFront(matrix, greenhouse.buildArea.y_min + 1, greenhouse.buildArea.y_min + GREENHOUSE_HEIGHT, greenhouse.buildArea.x_min, greenhouse.buildArea.x_max, greenhouse.buildArea.z_min, greenhouse.buildArea.z_max, used_glass)

    return greenhouse

def generateFront(matrix, h_min, h_max, x_min, x_max, z_min, z_max, used_glass):
    for x in range(x_min, x_max + 1):
        for y in range(h_min, h_max + 1):
            if x < x_min + 2 and y - h_min < 2 + (x - x_min):
                addGlass(matrix, y, x, z_min, z_max, used_glass)
            elif x > x_max - 2 and y - h_min < 2 + (x_max - x):
                addGlass(matrix, y, x, z_min, z_max, used_glass)
            elif x == x_min + 2 or x == x_max - 2 :
                if y - h_min < 3 :
                    addGlass(matrix, y, x, z_min, z_max, GLASS_ID)
                elif y - h_min == 3 :
                    addGlass(matrix, y, x, z_min, z_max, used_glass)
            elif x > x_min + 2 and x < x_max - 2:
                if y == h_max :
                    addGlass(matrix, y, x, z_min, z_max, used_glass)
                elif y == h_max - 1 :
                    addGlass(matrix, y, x, z_min, z_max, GLASS_ID)

def addGlass(matrix, y, x, z_min, z_max, glass) :
    matrix.setValue(y, x, z_min, glass)
    matrix.setValue(y, x, z_max, glass)

def generateGlassDome(matrix, h_min, h_max, x_min, x_max, z_min, z_max, used_glass):
    for x in range(x_min, x_max+1):
        for y in range(h_min, h_max+1):
            for z in range(z_min+1, z_max):
                if y - h_min == 1 + (x - x_min) or y - h_min == 1 + (x_max - x) :
                    matrix.setValue(y, x, z, used_glass)
                elif (x == x_min or x == x_max) and y == h_min :
                    matrix.setValue(y, x, z, used_glass)
                elif x > x_min + 3 and x < x_max - 3 and y == h_max :
                    matrix.setValue(y, x, z, used_glass)


def generateGroundAndCropse(matrix, h_min, x_min, x_max, z_min, z_max, foundation, ground):
    used_cropse = plants[RNG.randint(0, len(plants) - 1)]
    for x in range(x_min, x_max+1):
        for z in range(z_min, z_max+1):
            if x == x_min or x == x_max :
                matrix.setValue(h_min, x, z, foundation)
            elif z == z_min or z == z_max :
                if (x > x_min and x < x_min + 2) or (x < x_max and x > x_max - 2) :
                    matrix.setValue(h_min, x, z, foundation)
                elif x == x_min + 2 or x == x_max - 2 :
                    matrix.setValue(h_min, x, z, SEA_LANTERN_ID)
                else :
                    matrix.setValue(h_min, x, z, ground)
            elif x == x_min + 1 or x == x_max - 1 :
                if z == z_min + 3 or z == z_max - 3 :
                    matrix.setValue(h_min, x, z, WATER_ID)
                    #Put a dirt bloc under the water source and a trapdoor above
                    matrix.setValue(h_min - 1, x, z, DIRT_ID)
                    matrix.setValue(h_min + 1, x, z, TRAPDOOR_ID)
                else :
                    addFarmlandAndCrops(matrix, h_min, x, z, used_cropse)
            elif x == x_min + 2 or x == x_max - 2 :
                addFarmlandAndCrops(matrix, h_min, x, z, used_cropse)
            elif x == x_min + 3 or x == x_max - 3 :
                matrix.setValue(h_min, x, z, ground)
            else :
                addFarmlandAndCrops(matrix, h_min, x, z, used_cropse)

def addFarmlandAndCrops(matrix, h, x, z, used_cropse) :
    matrix.setValue(h, x, z, FARMLAND_ID)
    matrix.setValue(h + 1, x, z, used_cropse)


def getGreenHouseAreaInsideLot(h_min, h_max, x_min, x_max, z_min, z_max):
    remainder_x = x_max - x_min - GREENHOUSE_WIDTH
    x_min = x_min + (remainder_x / 2)
    x_max = x_max - (remainder_x / 2) - (remainder_x % 2) - 1
    remainder_z = z_max - z_min - GREENHOUSE_DEPTH
    z_min = z_min + (remainder_z / 2)
    z_max = z_max - (remainder_z / 2) - (remainder_z % 2) -1
    assert x_max - x_min == GREENHOUSE_WIDTH - 1
    assert z_max - z_min == GREENHOUSE_DEPTH - 1

    return (h_min, h_max, x_min, x_max, z_min, z_max)

def getOrientation():
    return "N"
