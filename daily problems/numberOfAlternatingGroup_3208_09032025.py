class Solution:
    def numberOfAlternatingGroups(self,colors, k):
        n = len(colors)
        count = 0
        alternating = 1

        for i in range(n + k - 2):
            if colors[i % n] == colors[(i - 1 + n) % n]:
                alternating = 1
            else:
                alternating += 1
            if alternating >= k:
                count += 1

        return count

solution = Solution()
print(solution.numberOfAlternatingGroups([0, 1, 0, 1, 0, 1], 2))  # Output: 6
print(solution.numberOfAlternatingGroups([0, 0, 1, 1], 3))  # Output: 0