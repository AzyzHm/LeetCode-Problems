class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        num_set = set(nums)
        n = len(nums)
        
        for i in range(2 ** n):
            bin_str = format(i, f'0{n}b')
            if bin_str not in num_set:
                return bin_str

print(Solution().findDifferentBinaryString(['01', '10']))  # Output: "00" or "11"
print(Solution().findDifferentBinaryString(['00', '01']))  # Output: "10" or "11"