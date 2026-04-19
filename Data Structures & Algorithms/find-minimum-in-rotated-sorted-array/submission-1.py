class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums[0], nums[1])

        mid_index = (len(nums) - 1) // 2
        if nums[0] > nums[mid_index]:
            return self.findMin(nums[:mid_index+1])
        elif nums[mid_index] > nums[-1]:
            return self.findMin(nums[mid_index:])
        elif nums[mid_index] > nums[mid_index + 1]:
            return self.findMin(nums[mid_index:])
        else:
            return self.findMin(nums[:mid_index+1])
