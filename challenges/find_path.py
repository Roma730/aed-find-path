import heapq
import math

from data_structures.city_map import CityMap


def find_path(
    city_map: CityMap,
    start: int,
    goal: int,
) -> list[int]:
    """
    Encontra o caminho de menor custo (menor número de ruas percorridas)
    entre `start` e `goal` usando A*.

    Cada rua (aresta) tem custo uniforme 1, refletindo o número de
    saltos entre interseções (não há peso/distância associado às ruas
    em `CityMap`).

    Por que não usar distância euclidiana como heurística aqui:
    como o custo de cada aresta é 1 (e não proporcional à distância
    geométrica entre interseções), uma heurística baseada em distância
    euclidiana pode superestimar o número real de saltos restantes
    sempre que as arestas do caminho ótimo forem geometricamente mais
    longas que outras arestas do mapa. Isso quebraria a admissibilidade
    e, portanto, a garantia de otimalidade do A*. Por isso a heurística
    usada é 0 (heurística nula), que é sempre admissível: o algoritmo
    continua sendo A*, mas se comporta como Dijkstra/busca uniforme,
    garantindo encontrar sempre o caminho ótimo (menor número de
    saltos).

    Retorna a lista de IDs de interseções do caminho, do `start` ao
    `goal` (inclusive). Retorna lista vazia se não houver caminho.
    Se start == goal, retorna [start].
    """
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