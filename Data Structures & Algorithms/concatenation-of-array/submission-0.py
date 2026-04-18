class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        array_length = len(nums)
        ans = [0]*(2 * array_length)
        for i in range(array_length):
            ans[i] = nums[i]
            ans[i+array_length] = nums[i]
        return ans