from __future__ import annotations

class Heap_Priority_Queue():
    def __init__(self, values: list[float]):
        self.queue: list[tuple[int, float]] = []
        self.pointerArray: list[int | None] = [None] * len(values) # index = vertex, value = place in binary heap
        for vertex, distance in enumerate(values):
            self.insert(vertex, distance)
        
    def insert(self, vertex: int, distance: float): # still need to add to pointerArray to remember where everything is
        self.queue.append((vertex, distance))
        currentIndex = len(self.queue) - 1
        self.percolate_up(currentIndex, vertex)

        
    def decrease_key(self, vertex: int, new_value: float):
        # find value
        indexInQueue = self.pointerArray[vertex]
        self.queue[indexInQueue] = (vertex, new_value) # type: ignore
        self.percolate_up(indexInQueue, vertex) # type: ignore
        print()
    
    def delete_min(self):
        # get values and pop 
        smallest = self.queue[0]
        self.queue[0] = self.queue[-1]
        self.queue.pop()

        if not self.is_not_empty():
            return smallest[0]

         # tell pointer array that vertex is out
        self.pointerArray[smallest[0]] = None
        
        # tell pointer array that prev last is now first
        self.pointerArray[self.queue[0][0]] = 0
        
        # percolate down
        self.percolate_down(0)

        # return og top value
        return smallest[0]

    def percolate_up(self, currentIndex: int, vertex: int):
        parentIndex = self.calculate_parent_index(currentIndex)
        self.pointerArray[vertex] = currentIndex

        while self.both_index_positive(currentIndex, parentIndex) and self.queue[currentIndex][1] < self.queue[parentIndex][1]:
            self.swap_places(currentIndex, parentIndex)
            currentIndex = parentIndex
            parentIndex = self.calculate_parent_index(currentIndex)
    
    def percolate_down(self, index: int):
        leftChild = 2 * index + 1
        rightChild = 2 * index + 2

        if leftChild > len(self.queue) - 1 or rightChild > len(self.queue) - 1:
            return
        
        if self.queue[leftChild][1] < self.queue[index][1]:
            self.swap_places(index, leftChild)
            self.percolate_down(leftChild)
        if self.queue[rightChild][1] < self.queue[index][1]:
            self.swap_places(index, rightChild)
            self.percolate_down(rightChild)
    
    def calculate_parent_index(self, index: int) -> int:
        return ((index - 1) // 2)
    
    def swap_places(self, firstIndex: int, secondIndex: int):
        # swap values in heap array
        firstValue = self.queue[firstIndex]
        secondValue = self.queue[secondIndex]
        self.queue[firstIndex] = secondValue
        self.queue[secondIndex] = firstValue

        # fix in pointer array
        self.pointerArray[firstValue[0]] = secondIndex
        self.pointerArray[secondValue[0]] =  firstIndex

    def both_index_positive(self, index1: int, index2: int) -> bool:
        return index1 >= 0 and index2 >= 0
        
    def is_not_empty(self):
        return len(self.queue) > 0


