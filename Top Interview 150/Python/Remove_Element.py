class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while(val in nums):
            nums.remove(val)
        return len(nums)

print(Solution().removeElement([3,2,2,3], 3)) # 2
print(Solution().removeElement([0,1,2,2,3,0,4,2], 2)) # 5
print(Solution().removeElement([3,3], 3)) # 0