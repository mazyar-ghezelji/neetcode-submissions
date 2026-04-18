class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                if nums[i] == nums[j] and i!=j:
                    return True
        return False
        