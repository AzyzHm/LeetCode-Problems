class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            else:
                continue
        
        count = 0
        while 0 in nums:
            nums.remove(0)
            count += 1
        
        while count > 0:
            nums.append(0)
            count -= 1
        
        return nums