class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def backtrack(current):
            if len(current) == n:
                result.append(current)
                return
            for char in 'abc':
                if not current or current[-1] != char:
                    backtrack(current + char)
        
        result = []
        backtrack("")
        
        if k > len(result):
            return ""
        return result[k - 1]

solution = Solution()
print(solution.getHappyString(1, 3))  # Output: "c"
print(solution.getHappyString(1, 4))  # Output: ""
print(solution.getHappyString(3, 9))  # Output: "cab"