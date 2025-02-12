class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        def digit_sum(n): # helper function to calculate the sum of the digits of a number
            return sum(int(digit) for digit in str(n))
        
        max_value = -1
        sum_dict = {} # used to store the maximum number for each digit sum.        
        for num in nums:
            s = digit_sum(num)
            if s in sum_dict:
                max_value = max(max_value, sum_dict[s] + num)
                sum_dict[s] = max(sum_dict[s], num)
            else:
                sum_dict[s] = num
        
        return max_value

print(Solution().maximumSum([18, 43, 36, 13, 7]))  # Output: 54
print(Solution().maximumSum([10, 12, 19, 14]))     # Output: -1
