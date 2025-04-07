class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        n = len(nums)
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[target]

# Example usage:
print(Solution().canPartition([1, 5, 11, 5]))  # Output: True
print(Solution().canPartition([1, 2, 3, 5]))   # Output: False