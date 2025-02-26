class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        max_sum = 0
        min_sum = 0
        current_sum = 0
        
        for num in nums:
            current_sum += num
            max_sum = max(max_sum, current_sum)
            min_sum = min(min_sum, current_sum)
        
        return max_sum - min_sum

solution = Solution()
print(solution.maxAbsoluteSum([1, -3, 2, 3, -4]))  # Output: 5
print(solution.maxAbsoluteSum([2, -5, 1, -4, 3, -2]))  # Output: 8