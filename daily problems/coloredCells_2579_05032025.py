class Solution:
    def coloredCells(self, n: int) -> int:
        # The number of colored cells after n steps can be calculated using the formula:
        # Total cells = 1 + 4 * (1 + 2 + 3 + ... + (n-1))
        # This is equivalent to the sum of the first (n-1) natural numbers multiplied by 4, plus 1.
        # The sum of the first (n-1) natural numbers is (n-1) * n / 2.
        return 1 + 4 * (n * (n - 1) // 2)

solution = Solution()
print(solution.coloredCells(1))  # Output: 1
print(solution.coloredCells(2))  # Output: 5
print(solution.coloredCells(3))  # Output: 13
print(solution.coloredCells(4))  # Output: 25