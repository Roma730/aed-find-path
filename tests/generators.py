from random import Random

from data_structures.city_map import CityMap

RANDOM_SEED = 42


def generate_city_map(size: int):
    random = Random(
        RANDOM_SEED + size
    )

    intersections = {}

    for node in range(size):

        intersections[node] = (
            random.random() * 1000,
            random.random() * 1000,
        )

    roads = {
        node: []
        for node in range(size)
    }

    for node in range(size - 1):

        roads[node].append(
            node + 1
        )

        roads[node + 1].append(
            node
        )

    extra_connections = max(
        size * 3,
        1,
    )

    for _ in range(
        extra_connections
    ):

        source = random.randint(
            0,
            size - 1,
        )

        target = random.randint(
            0,
            size - 1,
        )

        if source == target:
            continue

        if target not in roads[source]:

            roads[source].append(
                target
            )

            roads[target].append(
                source
            )

    city_map = CityMap(
        intersections=intersections,
        roads=roads,
    )

    return (
        city_map,
        0,
        size - 1,
    )


def generate_small_map():

    intersections = {
        0: (0, 0),
        1: (1, 0),
        2: (2, 0),
    }

    roads = {
        0: [1],
        1: [0, 2],
        2: [1],
    }

    city_map = CityMap(
        intersections=intersections,
        roads=roads,
    )

    return (
        city_map,
        0,
        2,
    )


def generate_disconnected_map():

    intersections = {
        0: (0, 0),
        1: (1, 0),
        2: (10, 0),
        3: (11, 0),
    }

    roads = {
        0: [1],
        1: [0],
        2: [3],
        3: [2],
    }

    city_map = CityMap(
        intersections=intersections,
        roads=roads,
    )

    return (
        city_map,
        0,
        3,
    )


def generate_reference_map():

    intersections = {
        0: (0, 0),
        1: (1, 1),
        2: (2, 1),
        3: (3, 0),
        4: (1, -1),
        5: (2, -1),
    }

    roads = {
        0: [1, 4],
        1: [0, 2],
        2: [1, 3],
        3: [2, 5],
        4: [0, 5],
        5: [4, 3],
    }

    city_map = CityMap(
        intersections=intersections,
        roads=roads,
    )

    return (
        city_map,
        0,
        3,
    )


def generate_single_node_map():

    intersections = {
        0: (0, 0),
    }

    roads = {
        0: [],
    }

    city_map = CityMap(
        intersections=intersections,
        roads=roads,
    )

    return (
        city_map,
        0,
        0,
    )
