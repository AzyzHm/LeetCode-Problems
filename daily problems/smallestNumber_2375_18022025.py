class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        result = []
        for i in range(len(pattern) + 1):
            stack.append(str(i + 1))
            if i == len(pattern) or pattern[i] == 'I':
                while stack:
                    result.append(stack.pop())
        return ''.join(result)

solution = Solution()
print(solution.smallestNumber("IIIDIDDD"))  # Output: "123549876"
print(solution.smallestNumber("DDD"))       # Output: "4321"