class MinHeap:
    def __init__(self):
        self.heap = []

    # ── helpers ──────────────────────────────────────────────
    def _parent(self, i):   return (i - 1) // 2
    def _left(self, i):     return 2 * i + 1
    def _right(self, i):    return 2 * i + 2
    def _swap(self, i, j):  self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _sift_up(self, i):
        """Bubble a node UP until the heap property is restored."""
        while i > 0:
            p = self._parent(i)
            if self.heap[i] < self.heap[p]:
                self._swap(i, p)
                i = p
            else:
                break

    def _sift_down(self, i):
        """Push a node DOWN until the heap property is restored."""
        n = len(self.heap)
        while True:
            smallest = i
            l, r = self._left(i), self._right(i)
            if l < n and self.heap[l] < self.heap[smallest]:
                smallest = l
            if r < n and self.heap[r] < self.heap[smallest]:
                smallest = r
            if smallest == i:
                break
            self._swap(i, smallest)
            i = smallest

    # ── public API ───────────────────────────────────────────
    def push(self, val):          # O(log n)
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self):                # O(log n)
        if not self.heap:
            return -1
        self._swap(0, len(self.heap) - 1)   # root ↔ last
        val = self.heap.pop()               # remove (old root)
        if self.heap:
            self._sift_down(0)              # restore order
        return val

    def top(self):                # O(1)
        return self.heap[0] if self.heap else -1

    def heapify(self, nums):      # O(n)
        self.heap = list(nums)
        # Start at last internal node and sift every node down.
        # This is Floyd's algorithm
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._sift_down(i)