from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        
        total_count = nums.count(candidate)
        if total_count <= len(nums) // 2:
            return -1
        
        left_count = 0
        for i in range(len(nums) - 1):
            if nums[i] == candidate:
                left_count += 1
            right_count = total_count - left_count
            if left_count > (i + 1) // 2 and right_count > (len(nums) - i - 1) // 2:
                return i
        
        return -1

print(Solution().minimumIndex([1, 2, 2, 2]))  # Output: 2
print(Solution().minimumIndex([2, 1, 3, 1, 1, 1, 7, 1, 1]))  # Output: 4
print(Solution().minimumIndex([3, 3, 3, 3, 7, 7, 7]))  # Output: -1