# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def quicksort_in_place(s: int, e: int):
            if e - s + 1 <= 1:
                return
            pivot = pairs[e]
            p = s
            for i in range(s, e):
                if pairs[i].key < pivot.key:
                    pairs[p], pairs[i] = pairs[i], pairs[p]
                    p += 1
            pairs[e], pairs[p] = pairs[p], pairs[e]
            quicksort_in_place(s, p - 1)
            quicksort_in_place(p + 1, e)
        
        quicksort_in_place(0, len(pairs) - 1)
        return pairs