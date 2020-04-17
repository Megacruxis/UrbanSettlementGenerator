import random
import math
import RNG
import logging
import utilityFunctions as utilityFunctions
from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox, level

WOOD_ID = [17, 162]
LEAF_ID = [18, 161]
GROUND_ID = [0, 1, 2, 3, 4, 12, 13, 78, 79, 82, 110]
AIR_ID = [0, 106, 127]
WOOD_NAME = {'17:0': 'oak', '17:1': 'spruce', '17:2': 'birch', '17:3': 'jungle', '162:0': 'acacia', '162:1': 'dark_oak'}

finded_wood = {'17:0': 0, '17:1': 0, '17:2': 0, '17:3': 0, '162:0': 0, '162:1': 0}

def determinate_usable_wood(level, height_map, x_min, x_max, z_min, z_max) :
    usable_wood = []
    for z in range(z_min, z_max):
        for x in range(x_min, x_max):
            y = height_map[x - x_min][z - z_min]
            block = level.blockAt(x, y, z)
            while block in WOOD_ID or block in LEAF_ID or (block in AIR_ID and y > 0) :
                if block in WOOD_ID :
                    sub_id = level.blockDataAt(x, y, z)
                    if (block == 17 and sub_id > 3) or (block == 162 and sub_id > 1) :
                        sub_id = 0
                    logging.info("trouver block id = {}:{} at coordinate x = {}, y = {}, z = {}".format(block, sub_id, x_min + x, y, z_min + z))
                    finded_wood[str(block) + ':' + str(sub_id)] += 1
                y = y - 1
                block = level.blockAt(x, y, z)

    logging.info("---------------------------------------------")
    logging.info("finded wood : oak : {}, spruce {}, birch {}, jungle {}, acacia {}, dark_oak {}".format(finded_wood['17:0'], finded_wood['17:1'], finded_wood['17:2'], finded_wood['17:3'], finded_wood['162:0'], finded_wood['162:1']))
    logging.info("---------------------------------------------")

    for key in finded_wood.keys():
        """ Todo add a better condition """
        if finded_wood[key] > 0 :
            usable_wood.append(WOOD_NAME[key])

    if len(usable_wood) == 0 :
        usable_wood.append('spruce')
    logging.info("usable wood = {}".format(usable_wood))
    return usable_wood
