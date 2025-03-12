class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        count_neg = 0
        count_pos = 0
        for num in nums:
            if num < 0:
                count_neg += 1
            elif num > 0:
                count_pos += 1
            else:
                continue
        return max(count_pos,count_neg)
    

solution = Solution()
print(solution.maximumCount([-2, -1, -1, 1, 2, 3]))  # Output: 3
print(solution.maximumCount([0, 0, 0, 0]))  # Output: 0
print(solution.maximumCount([-1, -2, -3, -4, -5]))  # Output: 5
        