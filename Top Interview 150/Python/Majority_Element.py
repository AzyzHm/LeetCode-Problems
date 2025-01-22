class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        unique_nums = set(nums)
        max = 0
        max_num = 0
        for num in unique_nums:
            if nums.count(num) > max:
                max = nums.count(num)
                max_num = num
        return max_num

print(Solution().majorityElement([3,2,3])) # 3
print(Solution().majorityElement([2,2,1,1,1,2,2])) # 2
print(Solution().majorityElement([1])) # 1
print(Solution().majorityElement([6,5,5])) # 5