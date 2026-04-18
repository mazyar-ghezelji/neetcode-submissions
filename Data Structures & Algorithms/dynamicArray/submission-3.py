class DynamicArray:
    def __init__(self, capacity: int):
        """Initialize with a fixed capacity"""
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity
    
    def get(self, i: int) -> int:
        """Get element at index i"""
        return self.arr[i]
    
    def set(self, i: int, n: int) -> None:
        """Set element at index i to n"""
        self.arr[i] = n
    
    def pushback(self, n: int) -> None:
        """Add element to the end of array"""
        # If array is full, resize first!
        if self.size == self.capacity:
            self.resize()
        
        # Add element at the end
        self.arr[self.size] = n
        self.size += 1
    
    def popback(self) -> int:
        """Remove and return the last element"""
        # Decrease size first
        self.size -= 1
        # Return the element that was at the end
        return self.arr[self.size]
    
    def resize(self) -> None:
        """Double the capacity of the array"""
        self.capacity *= 2
        new_arr = [0] * self.capacity
        
        # Copy existing elements to new array
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        
        self.arr = new_arr
    
    def getSize(self) -> int:
        """Return number of elements in array"""
        return self.size
    
    def getCapacity(self) -> int:
        """Return capacity of array"""
        return self.capacity