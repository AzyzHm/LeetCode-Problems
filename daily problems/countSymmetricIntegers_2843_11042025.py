class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high + 1):
            str_i = str(i)
            if len(str_i) % 2 == 0:
                mid = len(str_i) // 2
                left_sum = sum(int(digit) for digit in str_i[:mid])
                right_sum = sum(int(digit) for digit in str_i[mid:])
                if left_sum == right_sum:
                    count += 1
        return count
    
# Example usage:
print(Solution().countSymmetricIntegers(1, 100))  # Output: 9
