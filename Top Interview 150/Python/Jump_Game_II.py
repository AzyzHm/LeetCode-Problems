class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        jumps, max_reach, steps = 0, 0, 0
        for i in range(len(nums) - 1):
            max_reach = max(max_reach, i + nums[i]) # find the maximum reach
            if i == steps: # if we reach the end of the current steps we need to jump
                jumps += 1
                steps = max_reach
        return jumps

print(Solution().jump([2,3,1,1,4]))  # 2
print(Solution().jump([2,3,0,1,4]))  # 2
print(Solution().jump([3,2,1,0,4]))  # 2