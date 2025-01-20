class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()
        print(nums1)

Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3)