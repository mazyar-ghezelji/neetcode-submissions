import heapq

class MedianFinder:
    def __init__(self):
        self.lower = []  # max-heap (store negatives)
        self.upper = []  # min-heap

    def addNum(self, num: int) -> None:
        # Step 1: push onto lower (negate for max-heap behavior)
        heapq.heappush(self.lower, -num)

        # Step 2: move lower's top to upper (negate back to positive)
        heapq.heappush(self.upper, -heapq.heappop(self.lower))

        # Step 3: rebalance if upper got bigger than lower
        if len(self.upper) > len(self.lower):
            heapq.heappush(self.lower, -heapq.heappop(self.upper))

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return -self.lower[0]          # odd count: lower's top is the median
        return (-self.lower[0] + self.upper[0]) / 2.0   # even count: average the two tops