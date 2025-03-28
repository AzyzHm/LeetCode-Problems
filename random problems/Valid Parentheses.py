def main():
    def isValid(s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
    print(isValid("()")) # True
    print(isValid("()[]{}")) # True
    print(isValid("(]")) # False

if __name__ == "__main__":
    main()