class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        def can_distribute(mid):
            # Check if it's possible to distribute `mid` candies to each child
            total = 0
            for candy in candies:
                total += candy // mid
                if total >= k:
                    return True
            return False

        # Binary search for the maximum number of candies per child
        left, right = 1, sum(candies) // k
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if can_distribute(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result

solution = Solution()
print(solution.maximumCandies([5, 8, 6], 3))  # Output: 5
print(solution.maximumCandies([2, 5], 11))    # Output: 0
