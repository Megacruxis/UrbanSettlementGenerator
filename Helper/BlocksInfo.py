CACTUS_ID = 81
TRAPDOOR_ID = 96
BROWN_MUSHROOM_ID = 99
RED_MUSHROOM_ID = 100
VINES_ID = 106
COCOA_ID = 127
DOUBLE_PLANT = 175
LOGS_ID = [17, 162]
LEAVES_ID = [18, 161]

AIR_ID = (0, 0)
STONE_ID = (1, 0)
GRASS_ID = (2, 0)
DIRT_ID = (3, 0)
PODZOL_ID = (3, 2)
WATER_ID = (9, 0)
SAND_ID = (12, 0)
RED_SAND_ID = (12, 1)
GRAVEL_ID = (13, 0)
COAL_ORE_ID = (16, 0)
GLASS_ID = (20, 0)
DEAD_BUSH_ID = (31, 0)
FARMLAND_ID = (60, 0)
SNOW_ID = (78, 0)
ICE_ID = (79, 0)
IRON_BAR_ID = (101, 0)
MYCELIUM_ID = (110, 0)
LILY_PAD_ID = (111, 0)
ACACIA_LOG = (162, 0)
SEA_LANTERN_ID = (169, 0)
TERRACOTTA_ID = (172, 0)

CROPS_ID = [(59, 0), (141, 0), (142, 0)]
BADLANDS_TERRACOTTA_ID = [(159, 0), (159, 1), (159, 4), (159, 8), (159, 12), (159, 14), (172, 0)]

WOOD_NAME = {(17, 0) : 'oak',
             (17, 1) : 'spruce',
             (17, 2) : 'birch',
             (17, 3) : 'jungle',
             (162, 0) : 'acacia',
             (162, 1) : 'dark_oak'}

LEAVES_TO_LOGS = {(18, 0) : (17, 0),
                  (18, 1) : (17, 1),
                  (18, 2) : (17, 2),
                  (18, 3) : (17, 3),
                  (161, 0) : (162, 0),
                  (161, 1) : (162, 1)}

PAVEMENT_ID = {'Base' : (1, 6),
               'Desert' : (24, 0),
               'Beach' : (5, 2),
               'Badlands' : (159, 8), #159, 12
               'Mushroom_fields' : (159, 10),
               'Mountains' : (1, 4),
               'Swamp' : (4, 0),
               'Jungle' : (208, 0)}

# with the id of the ground block you obtain the id of the corresponding underground block
UNDERGROUND_BLOCK_ID = {(1, 0) : (1, 0),
                        (2, 0) : (3, 0),
                        (3, 0) : (3, 0),
                        (3, 1) : (3, 1),
                        (3, 2) : (3, 0),
                        (12, 0) : (24, 0),
                        (12, 1) : (172, 0),
                        (13, 0) : (1, 0),
                        (16, 0) : (1, 0),
                        (79, 0) : (79, 0),
                        (80, 0) : (80, 0),
                        (82, 0) : (1, 0),
                        (110, 0) : (3, 0)}

WOOD_ID = {'oak': (17, 0),
           'spruce': (17, 1),
           'birch': (17, 2),
           'jungle': (17, 3),
           'acacia': (162, 0),
           'dark_oak': (162, 1)}

PLANKS_ID = {'oak': (5, 0),
             'spruce': (5, 1),
             'birch': (5, 2),
             'jungle': (5, 3),
             'acacia': (5, 4),
             'dark_oak': (5, 5)}

PLANTS_ID = {'oak': (18, 0),
            'spruce': (18, 1),
            'birch': (18, 2),
            'jungle': (18, 3),
            'acacia': (161, 0),
            'dark_oak': (161, 1),
            'Desert' : (81, 0),
            'Badlands' : (81, 0),
            'Mountains' : (18, 1)}

BUSH_ID = {'oak': (18, 0),
           'spruce': (18, 1),
           'birch': (18, 2),
           'jungle': (18, 3),
           'acacia': (161, 0),
           'dark_oak': (161, 1),
           'Desert' : (24, 1),
           'Badlands' : (179, 1),
           'Mountains' : (18, 1)}

FENCE_ID = {'oak': (85, 0),
            'spruce': (188, 0),
            'birch': (189, 0),
            'jungle': (190, 0),
            'acacia': (192, 0),
            'dark_oak': (191, 0),
            'iron_bar' : (101, 0)}

STAIRS_ID = {'oak': (53, 0),
            'spruce': (134, 0),
            'birch': (135, 0),
            'jungle': (136, 0),
            'acacia': (163, 0),
            'dark_oak': (164, 0),
            'Desert' : (128, 0),
            'Badlands' : (180, 0),
            'Mountains' : (67, 0)}

UPPER_SLAB_ID = {'oak': (126, 8),
                 'spruce': (126, 9),
                 'birch': (126, 10),
                 'jungle': (126, 11),
                 'acacia': (126, 12),
                 'dark_oak': (126, 13),
                 'Desert' : (44, 9),
                 'Badlands' : (182, 8),
                 'Mountains' : (44, 11)}

LOWER_SLAB_ID = {'oak': (126, 0),
                 'spruce': (126, 1),
                 'birch': (126, 2),
                 'jungle': (126, 3),
                 'acacia': (126, 4),
                 'dark_oak': (126, 5),
                 'Desert' : (44, 1),
                 'Badlands' : (182, 0),
                 'Mountains' : (44, 3)}

STRUCTURE_BLOCK_ID = {'Desert' : (24, 0),
                      'Badlands' : (179, 0),
                      'Mountains' : (4, 0)}

FLOWERS_ID = {'Desert' : [(32, 0), (81, 0)],
              'Badlands' : [(32, 0), (81, 0)],
              'Base' : [(38, 0), (37, 0), (38, 3), (38, 4), (38, 5), (38, 6), (38, 7), (38, 8)],
              'Mountains' : [(38, 0), (37, 0), (38, 2), (38, 2)],
              'Swamp' : [(38, 1), (38, 1), (38, 1), (38, 0), (37, 0)],
              'Snowy_zone' : [(78, 0), (78, 1), (78, 2), (0, 0)],
              'Mushroom_fields' : [(39, 0), (40, 0), (0, 0)]}

PLANT_GROUND_ID = {'Base' : (2, 0),
                   'Desert' : (12, 0),
                   'Badlands' : (12, 1),
                   'Mushroom_fields' : (110, 0)}

HOUSE_FLOOR_ID = {'oak': (18, 0),
                  'spruce': (18, 1),
                  'birch': (18, 2),
                  'jungle': (18, 3),
                  'acacia': (161, 0),
                  'dark_oak': (161, 1),
                  'Desert' : (24, 0),
                  'Badlands' : (179, 0),
                  'Base' : (43, 0)}

HOUSE_WALL_ID = {'Mountains': [(4, 0), (1, 1), (1, 3), (1, 5), (45, 0), (112, 0)],
                 'Desert': [(24, 0), (24, 2)],
                 'Badlands': [(179, 0), (179, 2)],
                 'Base' : [(98, 0), (-1, 0), (45, 0), (112, 0), (155, 0)],
                 'Snowy_zone' : [(80, 0), (98, 0), (-1, 0), (45, 0), (112, 0), (155, 0)],
                 'Swanp' : [(48, 0), (-1, 0), (4, 0), (112, 0)],
                 'Beach' : [(-1, 0)]}

# with the id of the wall you obtain the id of the corresponding pillar
HOUSE_PILLAR_ID = {(80, 0) : (0, 0),
                   (1, 1) : (1, 2),
                   (1, 3) : (1, 4),
                   (1, 5) : (1, 6),
                   (24, 0) : (24, 1),
                   (24, 2) : (24, 1),
                   (179, 0) : (179, 1),
                   (179, 2) : (179, 1),
                   (98, 0) : (98, 3),
                   (112, 0) : (159, 15),
                   (155, 0) : (155, 2),
                   (45, 0) : (1, 2),
                   (114, 0) : (179, 2)}

GREENHOUSE_GLASS_ID = {'Base' : [(95, 0)],
                       'Desert' : [(95, 0), (95, 0), (95, 4), (95, 4), (95, 4)],
                       'Badlands' : [(95, 0), (95, 0), (95, 1), (95, 1), (95, 1)],
                       'Mushroom_fields' : [(95, 0), (95, 12)],
                       'Jungle' : [(95, 0), (95, 0), (95, 5), (95, 5), (95, 5)],
                       'Swanp' : [(95, 0), (95, 13)]}

GREENHOUSE_GROUND_ID = {'Base' : (208, 0),
                        'Desert' : (24, 0),
                        'Beach' : (24, 0),
                        'Badlands' : (179, 0),
                        'Mushroom_fields' : (110, 0)}

GREENHOUSE_FUNDATION_ID = {'Desert' : (24, 0),
                           'Badlands' : (179, 0),
                           'Mountains' : (4, 0),
                           'Swamp' : (48, 0)}

WELL_WALL_ID = {'Desert' : (24, 2),
                'Badlands' : (179, 2)}
