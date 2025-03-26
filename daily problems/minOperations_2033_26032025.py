from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flattened = [num for row in grid for num in row]
        remainder = flattened[0] % x
        for num in flattened:
            if num % x != remainder:
                return -1
        flattened.sort()
        median = flattened[len(flattened) // 2]
        operations = 0
        for num in flattened:
            operations += abs(num - median) // x
        return operations

print(Solution().minOperations([[2, 4], [6, 8]], 2))  # Output: 4
print(Solution().minOperations([[1, 5], [2, 3]], 1))  # Output: 5
print(Solution().minOperations([[1, 2], [3, 4]], 2))  # Output: -1