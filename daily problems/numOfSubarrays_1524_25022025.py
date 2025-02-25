class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        odd_count = 0
        even_count = 1  # To handle subarrays starting from the beginning
        current_sum = 0
        result = 0
        
        for num in arr:
            current_sum += num
            if current_sum % 2 == 0:
                result += odd_count
                even_count += 1
            else:
                result += even_count
                odd_count += 1
            result %= MOD
        
        return result

solution = Solution()
print(solution.numOfSubarrays([1, 3, 5]))  # Output: 4
print(solution.numOfSubarrays([2, 4, 6]))  # Output: 0
print(solution.numOfSubarrays([1, 2, 3, 4, 5, 6, 7]))  # Output: 16