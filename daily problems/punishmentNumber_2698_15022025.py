class Solution:
    def punishmentNumber(self, n: int) -> int:
        # Helper function to check if a number's square can be partitioned
        def can_partition(s: str, target: int) -> bool:
            if not s:
                return target == 0
            current = 0
            for i in range(len(s)):
                current = current * 10 + int(s[i])
                if current > target:
                    break
                if can_partition(s[i + 1:], target - current):
                    return True
            return False

        total_sum = 0
        for i in range(1, n + 1):
            square_str = str(i * i)
            if can_partition(square_str, i):
                total_sum += i * i
        return total_sum

solution = Solution()
print(solution.punishmentNumber(10))  # Output: 182
print(solution.punishmentNumber(37))  # Output: 1478