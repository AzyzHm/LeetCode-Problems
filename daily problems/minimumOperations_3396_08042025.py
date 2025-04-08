class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        if len(set(nums)) == len(nums):
            return 0
        else:
            output = 0
            while len(nums) > 3:
                nums.pop(0)
                nums.pop(0)
                nums.pop(0)

                if len(set(nums)) == len(nums):
                    return output + 1
                else:
                    output += 1
            return output  if (len(set(nums)) == len(nums)) or (len(nums) == 0) else output+1
        
# Example usage:
print(Solution().minimumOperations([1, 2, 3, 4, 5]))  # Output: 0
print(Solution().minimumOperations([1, 2, 2, 3, 4]))  # Output: 1