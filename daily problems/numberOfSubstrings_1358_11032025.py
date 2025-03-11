class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = { 'a': 0, 'b': 0, 'c': 0 }
        left = 0
        result = 0
        
        for right in range(len(s)):
            count[s[right]] += 1
            
            while all(count[char] > 0 for char in ('a', 'b', 'c')):
                count[s[left]] -= 1
                left += 1
            
            result += left
        
        return result

solution = Solution()
print(solution.numberOfSubstrings("abcabc"))  # Output: 10
print(solution.numberOfSubstrings("aaacb"))   # Output: 3
print(solution.numberOfSubstrings("abc"))     # Output: 1