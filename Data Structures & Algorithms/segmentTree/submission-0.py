class SegmentTree:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        # tree stored in an array of size 2n; leaves at [n, 2n)
        self.tree = [0] * (2 * self.n)
        # place leaves
        for i, v in enumerate(nums):
            self.tree[self.n + i] = v
        # build internal nodes bottom-up
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index: int, val: int) -> None:
        i = self.n + index          # jump to the leaf
        self.tree[i] = val
        # propagate the change up to the root
        while i > 1:
            i //= 2
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def query(self, L: int, R: int) -> int:
        # convert to leaf indices; make R exclusive
        l, r = self.n + L, self.n + R + 1
        total = 0
        while l < r:
            if l % 2 == 1:      # l is a right child → include it, move right
                total += self.tree[l]
                l += 1
            if r % 2 == 1:      # r is a right child boundary → step back, include
                r -= 1
                total += self.tree[r]
            l //= 2
            r //= 2
        return total