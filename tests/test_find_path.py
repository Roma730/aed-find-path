from challenges.find_path import (
    find_path,
)

from tests.generators import (
    generate_small_map,
    generate_reference_map,
    generate_disconnected_map,
    generate_single_node_map,
    generate_city_map,
)


def is_valid_path(
    city_map,
    path,
    start,
    goal,
):

    if not path:
        return False

    if path[0] != start:
        return False

    if path[-1] != goal:
        return False

    intersections = city_map.intersections
    roads = city_map.roads

    for node in path:

        if node not in intersections:
            return False

    for current, next_ in zip(
        path,
        path[1:],
    ):

        if next_ not in roads[current]:
            return False

    return True


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

    assert path == [0]


def test_small_map():

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

    assert is_valid_path(
        city_map,
        path,
        start,
        goal,
    )


def test_reference_map():

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

    assert is_valid_path(
        city_map,
        path,
        start,
        goal,
    )


def test_no_solution():

    (
        city_map,
        start,
        goal,
    ) = generate_disconnected_map()

    path = find_path(
        city_map,
        start,
        goal,
    )

    assert path == []


def test_start_is_first_node():

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

    assert path[0] == start


def test_goal_is_last_node():

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

    assert path[-1] == goal


def test_all_nodes_exist():

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

    for node in path:

        assert (
            node
            in city_map.intersections
        )


def test_all_edges_are_valid():

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

    for current, next_ in zip(
        path,
        path[1:],
    ):

        assert (
            next_
            in city_map.roads[current]
        )


def test_medium_map():

    (
        city_map,
        start,
        goal,
    ) = generate_city_map(
        100
    )

    path = find_path(
        city_map,
        start,
        goal,
    )

    assert is_valid_path(
        city_map,
        path,
        start,
        goal,
    )


def test_large_map():

    (
        city_map,
        start,
        goal,
    ) = generate_city_map(
        500
    )

    path = find_path(
        city_map,
        start,
        goal,
    )

    assert is_valid_path(
        city_map,
        path,
        start,
        goal,
    )
