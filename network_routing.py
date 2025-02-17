from array_priority_queue import Array_Priority_Queue
from heap_priority_queue import Heap_Priority_Queue

def find_shortest_path_with_heap(
        graph: dict[int, dict[int, float]],
        source: int,
        target: int
) -> tuple[list[int], float]:
    """
    Find the shortest (least-cost) path from `source` to `target` in `graph`
    using the heap-based algorithm.

    Return:
        - the list of nodes (including `source` and `target`)
        - the cost of the path
    """
    num_verticies = len(graph.keys())
    prev: list[int | None] = [None] * num_verticies
    dist: list[float] = [float('inf')] * num_verticies # index = vertex, value = distance from start
    dist[source] = 0
    # make the queue
    pq = Heap_Priority_Queue(dist)
    return find_shortest_path(graph, source, target, pq, prev, dist)

def find_shortest_path_with_array(
        graph: dict[int, dict[int, float]],
        source: int,
        target: int
) -> tuple[list[int], float]:
    """
    Find the shortest (least-cost) path from `source` to `target` in `graph`
    using the array-based (linear lookup) algorithm.

    Return:
        - the list of nodes (including `source` and `target`)
        - the cost of the path
    """
    num_verticies = len(graph.keys())
    prev: list[int | None] = [None] * num_verticies
    dist: list[float] = [float('inf')] * num_verticies # index = vertex, value = distance from start
    dist[source] = 0
    # make the queue
    pq = Array_Priority_Queue(dist)
    return find_shortest_path(graph, source, target, pq, prev, dist)

def find_shortest_path(
        graph: dict[int, dict[int, float]],
        source: int,
        target: int, 
        pq: Array_Priority_Queue | Heap_Priority_Queue,
        prev: list[int | None],
         dist: list[float]
) -> tuple[list[int], float]:
    while pq.is_not_empty(): # shoudl be while queue not empty
        current_vertex = pq.delete_min() # should be delete min from queue
        for edge in graph[current_vertex]:
            currentDistance: float = dist[edge]
            potentialNewDistance = graph[current_vertex][edge] + dist[current_vertex]
            if currentDistance > potentialNewDistance:
                prev[edge] = current_vertex
                dist[edge] = potentialNewDistance
                pq.decrease_key(edge, potentialNewDistance)

    cost: float = dist[target]
    path = find_path(target, prev)
    return (path, cost)

def find_path(target: int, prev: list[int | None]) -> list[int]:
    path: list[int] = [target]
    current_index = target
    while prev[current_index] != None:
        path.append(prev[current_index]) # type: ignore
        current_index = prev[current_index] # type: ignore
    path.reverse()
    return path