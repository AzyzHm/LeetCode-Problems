from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        diff = [0] * (n + 1)
        decrement = 0
        k = 0

        for i in range(n):
            while decrement + diff[i] < nums[i]:
                if k == len(queries):
                    return -1
                l, r, val = queries[k]
                k += 1
                if r < i:
                    continue
                diff[max(l, i)] += val
                if r + 1 < n:
                    diff[r + 1] -= val
            decrement += diff[i]

        return k

# Example usage:
solution = Solution()
print(solution.minZeroArray([2,0,2], [[0,2,1],[0,2,1],[1,1,3]]))  # Output: 2