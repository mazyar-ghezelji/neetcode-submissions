from typing import List, Optional

class TreeMap:
    
    class TreeNode:
        def __init__(self, key: int, val: int):
            self.key = key
            self.val = val
            self.left: Optional['TreeMap.TreeNode'] = None
            self.right: Optional['TreeMap.TreeNode'] = None

    def __init__(self):
        self.root: Optional[TreeMap.TreeNode] = None

    def insert(self, key: int, val: int) -> None:
        self.root = self._insert(self.root, key, val)

    def _insert(self, node: Optional[TreeNode], key: int, val: int) -> Optional[TreeNode]:
        if not node:
            return TreeMap.TreeNode(key, val)
        
        if key < node.key:
            node.left = self._insert(node.left, key, val)
        elif key > node.key:
            node.right = self._insert(node.right, key, val)
        else:
            # Update value if key already exists
            node.val = val
        return node

    def get(self, key: int) -> int:
        node = self._get_node(self.root, key)
        return node.val if node else -1

    def _get_node(self, node: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not node:
            return None
        if key < node.key:
            return self._get_node(node.left, key)
        elif key > node.key:
            return self._get_node(node.right, key)
        else:
            return node

    def getMin(self) -> int:
        if not self.root:
            return -1
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.val

    def getMax(self) -> int:
        if not self.root:
            return -1
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.val

    def remove(self, key: int) -> None:
        self.root = self._remove(self.root, key)

    def _remove(self, node: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not node:
            return None

        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            # Node to be deleted found
            if not node.left and not node.right:
                return None
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            
            # Node with two children: get inorder successor
            successor = node.right
            while successor.left:
                successor = successor.left
            
            node.key = successor.key
            node.val = successor.val
            node.right = self._remove(node.right, successor.key)
        
        return node

    def getInorderKeys(self) -> List[int]:
        result: List[int] = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node: Optional[TreeNode], result: List[int]) -> None:
        if not node:
            return
        self._inorder(node.left, result)
        result.append(node.key)
        self._inorder(node.right, result)