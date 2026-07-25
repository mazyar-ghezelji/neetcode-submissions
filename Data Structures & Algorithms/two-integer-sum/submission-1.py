class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # L = 0
        # R = len(nums)-1
        # assuming it is sorted
        # while L < R:
        #     sums = nums[L]+ nums[R]
        #     if sums == target:
        #         return [L,R]
        #     elif sums < target:
        #         L += 1
        #     else:
        #         R -= 1
        for l in range(len(nums)):
            for r in range(l+1, len(nums)):
                sums = nums[l]+ nums[r]
                if sums == target:
                    return [l,r]
                
        
        