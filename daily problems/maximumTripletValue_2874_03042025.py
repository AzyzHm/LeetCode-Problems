from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_i = nums[0]
        max_triplet_value = 0
        max_suffix = [0] * n

        max_suffix[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            max_suffix[i] = max(max_suffix[i + 1], nums[i])

        for j in range(1, n - 1):
            max_i = max(max_i, nums[j - 1])
            if max_i > nums[j]:
                max_triplet_value = max(max_triplet_value, (max_i - nums[j]) * max_suffix[j + 1])

        return max_triplet_value

solution = Solution()
print(solution.maximumTripletValue([1, 2, 3, 4]))  # Output: 0
print(solution.maximumTripletValue([4, 1, 3, 2]))  # Output: 9