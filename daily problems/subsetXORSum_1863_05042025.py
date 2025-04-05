from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(idx, current_xor):
            if idx == len(nums):
                return current_xor
            
            include = backtrack(idx + 1, current_xor ^ nums[idx])
            exclude = backtrack(idx + 1, current_xor)
            
            return include + exclude
        
        return backtrack(0, 0)

# Example usage:
print(Solution().subsetXORSum([1, 3]))  # Output: 6
print(Solution().subsetXORSum([5, 1, 6]))  # Output: 28