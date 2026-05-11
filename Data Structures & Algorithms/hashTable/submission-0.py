class HashTable:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    def insert(self, key: int, value: int) -> None:
        if (self.size + 1) / self.capacity >= 0.5:
            self.resize()

        bucket = self.buckets[key % self.capacity]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.size += 1

    def get(self, key: int) -> int:
        bucket = self.buckets[key % self.capacity]
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> bool:
        bucket = self.buckets[key % self.capacity]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return True
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        for bucket in old_buckets:
            for key, value in bucket:
                self.insert(key, value)