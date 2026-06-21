import heapq
import math

from data_structures.city_map import CityMap


def find_path(
    city_map: CityMap,
    start: int,
    goal: int,
) -> list[int]:
    if start not in city_map.intersections or goal not in city_map.intersections:
        return []

    if start == goal:
        return [start]

    def heuristic(_node: int) -> float:
        return 0.0

    counter = 0  # desempate no heap, evita comparar tuplas com node igual
    open_heap = [(heuristic(start), counter, start)]

    came_from: dict[int, int] = {}
    g_score: dict[int, float] = {start: 0.0}
    closed: set[int] = set()

    while open_heap:
        _, _, current = heapq.heappop(open_heap)

        if current == goal:
            return _reconstruct_path(came_from, current)

        if current in closed:
            continue
        closed.add(current)

        for neighbor in city_map.roads.get(current, []):
            if neighbor in closed:
                continue

            tentative_g = g_score[current] + 1  # custo uniforme por aresta

            if tentative_g < g_score.get(neighbor, math.inf):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor)
                counter += 1
                heapq.heappush(open_heap, (f_score, counter, neighbor))

    return []  # goal inalcançável a partir de start


def _reconstruct_path(came_from: dict[int, int], current: int) -> list[int]:
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path
