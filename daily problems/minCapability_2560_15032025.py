class Solution:
    def minCapability(self,nums, k):
        def can_rob_with_capability(x):
            robbed_count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= x:
                    robbed_count += 1
                    i += 1  # Skip the next house to ensure non-adjacency
                i += 1
            return robbed_count >= k

        left, right = min(nums), max(nums)
        while left < right:
            mid = (left + right) // 2
            if can_rob_with_capability(mid):
                right = mid
            else:
                left = mid + 1
        return left
