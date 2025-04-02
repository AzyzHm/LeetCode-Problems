from typing import List
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_i = nums[0]
        max_triplet_value = 0

        for j in range(1, n - 1):
            max_i = max(max_i, nums[j - 1])
            for k in range(j + 1, n):
                triplet_value = (max_i - nums[j]) * nums[k]
                max_triplet_value = max(max_triplet_value, triplet_value)

        return max_triplet_value

print(Solution().maximumTripletValue([1, 2, 3, 4]))  # Output: 0
print(Solution().maximumTripletValue([4, 1, 3, 2]))  # Output: 9