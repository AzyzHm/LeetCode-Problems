class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        result = []
        temp = {}
        
        for nums in nums1:
            if nums[0] in temp:
                temp[nums[0]] += nums[1]
            else:
                temp[nums[0]] = nums[1]

        for nums in nums2:
            if nums[0] in temp:
                temp[nums[0]] += nums[1]
            else:
                temp[nums[0]] = nums[1]
        
        for key in sorted(temp.keys()):
            result.append([key, temp[key]])
    
        return result

solution = Solution()
print(solution.mergeArrays([[1, 2], [2, 3]], [[2, 1], [3, 4]]))  # Output: [[1, 2], [2, 4], [3, 4]]
print(solution.mergeArrays([[1, 3], [4, 5]], [[1, 2], [4, 1]]))  # Output: [[1, 5], [4, 6]]
