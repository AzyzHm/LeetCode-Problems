class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char.isdigit():
                if stack:
                    stack.pop()  # Remove the closest non-digit character on the left
            else:
                stack.append(char)
        
        return ''.join(stack)

print(Solution().clearDigits("abc"))  # Output: "abc"
print(Solution().clearDigits("cb34")) # Output: ""