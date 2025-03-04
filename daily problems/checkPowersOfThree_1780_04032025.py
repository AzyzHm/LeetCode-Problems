class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True

solution = Solution()
print(solution.checkPowersOfThree(12))  # Output: True (12 = 3^1 + 3^2)
print(solution.checkPowersOfThree(91))  # Output: True (91 = 3^0 + 3^2 + 3^4)
print(solution.checkPowersOfThree(21))  # Output: False