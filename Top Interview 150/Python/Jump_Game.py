class Solution:
    def canJump(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            if nums[i] == 0:
                if i == len(nums) - 1:
                    return True
                for j in range(i - 1, -1, -1):
                    if nums[j] > i - j:
                        break
                else:
                    return False
        return True

print(Solution().canJump([2,3,1,1,4]))  # True
print(Solution().canJump([3,2,1,0,4]))  # False
print(Solution().canJump([0]))  # True
