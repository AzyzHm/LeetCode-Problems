# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        stack = []
        i = 0
        while i < len(traversal):
            level = 0
            while i < len(traversal) and traversal[i] == '-':
                level += 1
                i += 1
            value = 0
            while i < len(traversal) and traversal[i].isdigit():
                value = value * 10 + int(traversal[i])
                i += 1
            node = TreeNode(value)
            if level == len(stack):
                if stack:
                    stack[-1].left = node
            else:
                while level != len(stack):
                    stack.pop()
                stack[-1].right = node
            stack.append(node)
        return stack[0]

solution = Solution()
root = solution.recoverFromPreorder("1-2--3--4-5--6--7")