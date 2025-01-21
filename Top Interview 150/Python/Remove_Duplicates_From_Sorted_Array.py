class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)

print(Solution().removeDuplicates([1, 1, 2]))  # 2
print(Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))  # 5
print(Solution().removeDuplicates([1, 2]))  # 2
        