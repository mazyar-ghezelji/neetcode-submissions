class Solution:
    def __init__(self):
        self.max = 0
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return self.max
        R =1
        L=0
        while R < len(prices):
            if prices[R] <= prices[L]:
                L=R
                R+=1
            else:
                temp = prices[R]-prices[L]
                if temp>self.max:
                    self.max = temp
                R+=1
        return self.max
        