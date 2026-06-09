from collections import deque

from challenges.find_path import (
    find_path,
)

from tests.generators import (
    generate_small_map,
    generate_reference_map,
    generate_city_map,
    generate_single_node_map,
)


def shortest_distance(
    city_map,
    start,
    goal,
):
    queue = deque(
        [(start, 0)]
    )

    visited = {start}

    while queue:

        (
            current,
            distance,
        ) = queue.popleft()

        if current == goal:
            return distance

        for neighbor in city_map.roads[current]:

            if neighbor in visited:
                continue

            visited.add(
                neighbor
            )

            queue.append(
                (
                    neighbor,
                    distance + 1,
                )
            )

    return None


def path_cost(path):

    if not path:
        return None

    return len(path) - 1


def test_single_node_map():

    (
        city_map,
        start,
        goal,
    ) = generate_single_node_map()

    path = find_path(
        city_map,
        start,
        goal,
    )

    assert (
        path_cost(path)
        == 0
    )


def test_optimal_path_small_map():

    (
        city_map,
        start,
        goal,
    ) = generate_small_map()

    path = find_path(
        city_map,
        start,
        goal,
    )

    expected = shortest_distance(
        city_map,
        start,
        goal,
    )

    assert (
        path_cost(path)
        == expected
    )


def test_optimal_path_reference_map():

    (
        city_map,
        start,
        goal,
    ) = generate_reference_map()

    path = find_path(
        city_map,
        start,
        goal,
    )

    expected = shortest_distance(
        city_map,
        start,
        goal,
    )

    assert (
        path_cost(path)
        == expected
    )


def test_optimal_path_medium_map():

    (
        city_map,
        start,
        goal,
    ) = generate_city_map(
        250
    )

    path = find_path(
        city_map,
        start,
        goal,
    )

    expected = shortest_distance(
        city_map,
        start,
        goal,
    )

    assert (
        path_cost(path)
        == expected
    )


def test_optimal_path_large_map():

    (
        city_map,
        start,
        goal,
    ) = generate_city_map(
        1000
    )

    path = find_path(
        city_map,
        start,
        goal,
    )

    expected = shortest_distance(
        city_map,
        start,
        goal,
    )

    assert (
        path_cost(path)
        == expected
    )
