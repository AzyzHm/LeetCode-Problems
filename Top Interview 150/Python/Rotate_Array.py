class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums) # in case k > len(nums)
        nums[:] = nums[-k:] + nums[:-k] # rotate the list
        return nums

print(Solution().rotate([1,2,3,4,5,6,7], 3)) # [5,6,7,1,2,3,4]
print(Solution().rotate([-1,-100,3,99], 2)) # [3,99,-1,-100]
print(Solution().rotate([1,2], 3)) # [2,1]