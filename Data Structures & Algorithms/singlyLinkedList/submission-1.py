class LinkedList:
    
    def __init__(self):
        self.head = [None,None]
        self.tail = self.head
        self.size = 0
    
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        node = self.head[1]
        for i in range(index):
            node = node[1]
        return node[0]

    def insertHead(self, val: int) -> None:
        node = [val, self.head[1]]
        self.head[1] = node
        self.size += 1
        if self.size == 1:
            self.tail = node

    def insertTail(self, val: int) -> None:
        node = [val, None]
        if self.size == 0:
            self.head[1] = node
            self.tail = node
        else:
            self.tail[1] = node
            self.tail = node
        self.size += 1

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        prev_node = self.head
        i = 0
        while i < index:
            prev_node = prev_node[1]
            i += 1
        
        if self.tail == prev_node[1]:
            self.tail = prev_node
            
        prev_node[1] = prev_node[1][1]
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        values = []
        node = self.head[1]
        i = 0
        while i < self.size:
            values.append(node[0])
            node = node[1]
            i+=1
        return values