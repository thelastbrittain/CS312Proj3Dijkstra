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
    while pq.is_not_empty(): # will run through len(vertices) times
        current_vertex = pq.delete_min()  # with array is O(n), with heap is O(logn)
        for edge in graph[current_vertex]: # will end up going through all edges O(len(edges)), not each time, but in total
            currentDistance: float = dist[edge] # constant
            potentialNewDistance = graph[current_vertex][edge] + dist[current_vertex] # constant
            if currentDistance > potentialNewDistance: # constant
                prev[edge] = current_vertex # const
                dist[edge] = potentialNewDistance # const
                pq.decrease_key(edge, potentialNewDistance) # in array is const, in heap is O(logn)

    cost: float = dist[target] # const
    path = find_path(target, prev) # this is O(n)
    return (path, cost) 

def find_path(target: int, prev: list[int | None]) -> list[int]:
    path: list[int] = [target] # const
    current_index = target # const
    while prev[current_index] != None: # worst case goes through all = O(n)
        path.append(prev[current_index]) # type: ignore # const
        current_index = prev[current_index] # type: ignore # const
    path.reverse() # O(n)
    return path