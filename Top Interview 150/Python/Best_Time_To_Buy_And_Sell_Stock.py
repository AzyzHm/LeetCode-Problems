class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
    
print(Solution().maxProfit([7,1,5,3,6,4])) # 5
print(Solution().maxProfit([7,6,4,3,1])) # 0
print(Solution().maxProfit([1,2])) # 1