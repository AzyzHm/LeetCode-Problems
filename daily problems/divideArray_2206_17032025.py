from collections import Counter

class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        count = Counter(nums)
        for freq in count.values():
            if freq % 2 != 0:
                return False
        return True


print(Solution().divideArray([3,2,3,2,2,2]))  # True
print(Solution().divideArray([3,2,3,2,2,1]))  # False
print(Solution().divideArray([3,2,3,2,2,2,2]))  # False