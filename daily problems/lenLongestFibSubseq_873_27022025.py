class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        s = set(arr)  # Convert the array to a set for O(1) lookups
        n = len(arr)
        max_len = 0

        for i in range(n):
            for j in range(i + 1, n):
                x, y = arr[i], arr[j]
                length = 2
                while x + y in s:
                    x, y = y, x + y
                    length += 1
                max_len = max(max_len, length)

        return max_len if max_len > 2 else 0

solution = Solution()
print(solution.lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]))  # Output: 5
print(solution.lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18]))  # Output: 3
