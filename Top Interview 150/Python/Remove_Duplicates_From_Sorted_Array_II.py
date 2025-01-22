class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        while i < len(nums):
            if nums.count(nums[i]) > 2:
                nums.pop(i)
            else:
                i += 1
        return len(nums)

print(Solution().removeDuplicates([1, 1, 2]))  # 3
print(Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))  # 7
print(Solution().removeDuplicates([1, 1, 1, 2, 2, 3]))  # 5