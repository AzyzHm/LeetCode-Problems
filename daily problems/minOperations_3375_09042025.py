class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        if k > min(nums):
            return -1
        else:
            nums = set(nums)
            if k in nums:
                return len(nums) - 1
            else:
                return len(nums)
    
# Example usage:
print(Solution().minOperations([5,2,5,4,5], 2))  # Output: 2
print(Solution().minOperations([2,1,2], 2))  # Output: -1