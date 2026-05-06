class node:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
class Deque:
    
    def __init__(self):
        self.right_ptr = node()
        self.left_ptr = node()

        self.right_ptr.left = self.left_ptr
        self.left_ptr.right = self.right_ptr

    def isEmpty(self) -> bool:
        if self.right_ptr.left == self.left_ptr or self.left_ptr.right == self.right_ptr:
            return True
        else: 
            return False

    def append(self, value: int) -> None:
        new_node = node(value, self.right_ptr.left, self.right_ptr)
        self.right_ptr.left.right = new_node
        self.right_ptr.left = new_node

    def appendleft(self, value: int) -> None:
        new_node = node(value, self.left_ptr, self.left_ptr.right)
        self.left_ptr.right.left = new_node
        self.left_ptr.right = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        node = self.right_ptr.left
        node.left.right = self.right_ptr
        self.right_ptr.left = node.left
        return node.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        node = self.left_ptr.right
        node.right.left = self.left_ptr
        self.left_ptr.right = node.right
        return node.val
        
