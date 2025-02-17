class Array_Priority_Queue():
    def __init__(self, values: list[float]):
        self.storage: dict[int, float] = {} # key = vertex, value = cost
        self.queue: set[int] = set() # this is the queue of verticies
        for i in range(len(values)):
            self.insert(i, values)
    
    def insert(self, index, values):
        self.storage[index] = values[index]
        self.queue.add(index)
        
    def decrease_key(self, vertex: int, new_value: float):
        self.storage[vertex] = new_value
        print()

    def delete_min(self):
        # find smallest distance (value)
        smallest_distance = float("inf")
        smallest_vertex = 1
        for vertex in self.queue:
            if self.storage[vertex] < smallest_distance:
                smallest_distance = self.storage[vertex]
                smallest_vertex = vertex
        self.queue.remove(smallest_vertex)
        return smallest_vertex

    def is_not_empty(self):
        return len(self.queue) > 0