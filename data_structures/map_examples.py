from data_structures.city_map import CityMap


SMALL_MAP = CityMap(
    intersections={
        0: (0, 0),
        1: (1, 0),
        2: (2, 0),
    },
    roads={
        0: [1],
        1: [0, 2],
        2: [1],
    },
)


REFERENCE_MAP = CityMap(
    intersections={
        0: (0, 0),
        1: (1, 1),
        2: (2, 1),
        3: (3, 0),
        4: (1, -1),
        5: (2, -1),
    },
    roads={
        0: [1, 4],
        1: [0, 2],
        2: [1, 3],
        3: [2, 5],
        4: [0, 5],
        5: [4, 3],
    },
)


DISCONNECTED_MAP = CityMap(
    intersections={
        0: (0, 0),
        1: (1, 0),
        2: (10, 0),
        3: (11, 0),
    },
    roads={
        0: [1],
        1: [0],
        2: [3],
        3: [2],
    },
)


SINGLE_NODE_MAP = CityMap(
    intersections={
        0: (0, 0),
    },
    roads={
        0: [],
    },
)
