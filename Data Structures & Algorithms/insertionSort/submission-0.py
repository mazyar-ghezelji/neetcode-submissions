# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        arr = list(pairs)          # work on a copy of the references
        states = []

        for i in range(len(arr)):
            current = arr[i]
            j = i - 1
            # Strict '>' preserves stability: equal keys never swap order.
            while j >= 0 and arr[j].key > current.key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = current
            states.append(arr[:])   # shallow-copy snapshot after this insertion

        return states