class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [None] * (capacity if capacity > 0 else 1);
        self.size = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        # v = self.array[i]
        # self.capacity += 1
        # if v != -1:
        #     self.array[i] = n
        #     return
        # self.array.append(None)
        # for j in range(i, len(self.array)):
        #     if j + 1 >= len(self.array):
        #         return self.array
        #     tmp = self.array[j] 
        #     self.array[j] = self.array[j + 1]
        #     self.array[j + 1] = tmp
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.getCapacity() == self.size:
            self.resize()
        self.size += 1
        self.array[self.size-1] = n


    def popback(self) -> int:
        i = self.size-1
        removed = self.array[i]
        self.array[i] = None
        self.size -= 1
        return removed

    def resize(self) -> None:
        capacity = len(self.array)
        self.array = self.array + ([None] * capacity)

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return len(self.array)