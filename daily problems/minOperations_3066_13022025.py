class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        import heapq
        
        heapq.heapify(nums)
        num_op = 0
        
        while nums[0] < k and len(nums) > 1:
            smallest = heapq.heappop(nums)
            second_smallest = heapq.heappop(nums)
            new_element = min(smallest, second_smallest) * 2 + max(smallest, second_smallest)
            heapq.heappush(nums, new_element)
            num_op += 1
        
        if nums[0] < k:
            return -1
        
        return num_op

# Test cases
print(Solution().minOperations([2, 11, 10, 1, 3], 10))  # Output: 2
print(Solution().minOperations([1, 1, 2, 4, 9], 20))    # Output: 4
print(Solution().minOperations([1, 1, 1], 10))          # Output: -1